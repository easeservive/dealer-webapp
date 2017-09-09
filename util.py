import MySQLdb
import log_rotator
import datetime
import random

from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from core.models import ScheduledServices, ScheduledServiceDetails, ComplaintCode, SupportedCarBrands
from customer.models import OTPTransactionInfo, Vehicles
from jobcard.models import JCVehicleInfo, JCStatus, JCServiceDetails, JCStocksInfo, JCInvoiceAndLabourCost,JCRecommendedServices, JCOtherStocksInfo
from inventory.models import Inventory
from django.contrib.auth.models import User
import config
from easeservice.message_functions import send_text_message
from easeservice import global_constants
from easeservice.portal_functions import generate_confirmation_token

def fetch_vehicles(user):
    try:
        result = []
        vehicles = list(Vehicles.objects.filter(User = user))
        if vehicles:
            for vehicle in vehicles:
                veh_dict = {'type': vehicle.VehicleType,
                            'brand': vehicle.Brand,
                            'model': vehicle.Model,
                            'fuel_type': vehicle.FuelType,
                            'c_num': vehicle.ChasisNumber,
                            'man_year': vehicle.YearOfManufacture,
                            'reg_num': vehicle.RegNumber}
                result.append(veh_dict)
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
    return result


def generateOTP(user):
    try:
        tranID = "OTP" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '_' + str(random.randint(111, 999))
        otpValue = str(random.randint(111111, 999999))
        time = str(datetime.datetime.now())
        status = 0
        # trigger SMS
        OTPTransactionInfo.objects.create(User = user,
            TranID = tranID,
            OTPValue = otpValue,
            DateTime = time,
            VerificationStatus = status
        )

        # deactivate user until verification
        user_obj = User.objects.get(username = user)
        user_obj.is_active = 0
        user_obj.save()

        print("otpValue - %s" % otpValue)

        send_text_message(user, "EASE SERVICE OTP - %s" % otpValue)

        return 1, tranID

    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        return 0, ""


def generateVLINK(user_obj):

    user_obj.is_active = 0
    user_obj.save()

    #token = generate_confirmation_token()
    # use token to generate verification link
    # send sms to user with verification link
    
    return True


def isValidOPT(tranid, otpvalue):
    try:
        otp_obj = OTPTransactionInfo.objects.get(TranID = tranid)

        if otp_obj.OTPValue == otpvalue:
            otp_obj.VerificationStatus = '1'
            otp_obj.save()
            user_obj = User.objects.get(username = otp_obj.User)
            user_obj.is_active = 1
            user_obj.save()
            return True
        else:
            return False
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        return False


def resetPassword(username, passwd, tranid):
    try:
        otp_obj = OTPTransactionInfo.objects.get(TranID = tranid)
        updated_time = datetime.datetime.strptime(otp_obj.DateTime, "%Y-%m-%d %H:%M:%S.%f")
        time_now = datetime.datetime.now()
        time_diff = updated_time - time_now

        if otp_obj.VerificationStatus == '1' and (time_diff.seconds < 1800):
            u = User.objects.get(username=username)
            u.set_password(passwd)
            u.save()
            result = {"status": "success", "msg": "Password has been updated successfully."}
        else:
            result = {"status": "failure", "msg": "Invalid OTP"}
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "Something went wrong."}
    return result


def fetchScheduledServices(brand, model, fuel_type, km_ticked):
    try:
        serid_obj = ScheduledServices.objects.get(Brand__iexact = brand, Model__iexact = model, FuelType__iexact = fuel_type, MaxKM__gte = km_ticked, MinKM__lte = km_ticked)
        if serid_obj:
            service_id = serid_obj.ServiceIdentifier
        else:
            raise ObjectDoesNotExist
        print(serid_obj)
        sch_obj = ScheduledServiceDetails.objects.filter(ServiceIdentifier = service_id)
        services = []
        parts = []
        for obj in sch_obj:
            temp_dict = {}
            parts_list = obj.Parts.split(',')
            temp_dict[obj.ServiceInfo] = parts_list
            if parts_list != [""]:
                parts.extend(parts_list)
            services.append(temp_dict)
        result = {"status": "success", "services": services, "parts": parts }
    except ObjectDoesNotExist:
        result = {"status": "failure", "msg": "No scheduled mainenance availble for this model."}
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "Something went wrong."}
    return result


def getEstimate(parts, dealerid):
    try:
        if isinstance(eval(parts), list):
            estimate = []
            print(parts, dealerid)
            for part in eval(parts):
                try:
                    inv_obj = Inventory.objects.get(PartIdentifier = part['identifier'], DealerID__iexact = dealerid)
                    estimate_dict = {}
                    estimate_dict['description'] = inv_obj.Description
                    estimate_dict['unit_price'] = inv_obj.MRP
                    estimate_dict['total_price'] = float(inv_obj.MRP) * float(part['qty'])
                    estimate.append(estimate_dict)
                except ObjectDoesNotExist:
                    pass
            result = {"status": "success", "estimate": estimate}
        else:
            raise
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "Something went wrong."}
    return result


def getJobCard(jc_id, dealerid, invoice_details = False):
    try:
        veh_obj = JCVehicleInfo.objects.get(JobCardID = jc_id, DealerID = dealerid)
        jc_obj = JCStatus.objects.get(JobCardID__iexact = jc_id, DealerID__iexact = dealerid)

        # fetch other parts
        try:
            other_parts = JCOtherStocksInfo.objects.get(JobCardID__iexact = jc_id)
        except JCOtherStocksInfo.DoesNotExist:
            other_parts = None

        # fetch service details
        try:
            ser_obj = JCServiceDetails.objects.filter(JobCardID__iexact = jc_id, DealerID__iexact = dealerid)
        except JCServiceDetails.DoesNotExist:
            ser_obj = None

        # fetch stocks info
        try:
            spares_obj = JCStocksInfo.objects.filter(JobCardID__iexact = jc_id, DealerID__iexact = dealerid)
        except JCStocksInfo.DoesNotExist:
            spares_obj = None

        # fetch labour and cost info
        try:
            lab_cost_obj = JCInvoiceAndLabourCost.objects.get(JobCardID__iexact = jc_id, DealerID__iexact = dealerid)
        except JCInvoiceAndLabourCost.DoesNotExist:
            lab_cost_obj = None

        try:
            recomd_obj = JCRecommendedServices.objects.get(JobCardID__iexact = jc_id, DealerID__iexact = dealerid)
        except JCRecommendedServices.DoesNotExist:
            recomd_obj = None

        #if veh_obj and jc_obj and ser_obj:
        if veh_obj and jc_obj:   
            details = {}
            details['veh_num'] = veh_obj.VehicleNumber
            details['brand'] = veh_obj.Brand
            details['model'] = veh_obj.Model
            details['fuel_type'] = veh_obj.FuelType
            details['c_num'] = veh_obj.ChassisNumber
            details['cust_name'] = veh_obj.CustomerName
            details['cont_num'] = veh_obj.ContactNumber
            details['cont_address'] = veh_obj.Address
            details['km_ticked'] = veh_obj.KilometersTicked
            details['jc_id'] = veh_obj.JobCardID
            details['service_reminder_time'] = jc_obj.service_reminder_time

            #print("jc_obj.ServiceTypeId - %s" % jc_obj.ServiceTypeId)
            details['service_type'] = "%s - %s" % (global_constants.service_types[jc_obj.ServiceTypeId]['service_type'],
                global_constants.service_types[jc_obj.ServiceTypeId]['classification'])

            details['del_time'] = jc_obj.DeliveryTime
            details['status'] = jc_obj.Status
            details['reason'] = jc_obj.PendingReason
            details['mechanic_name'] = jc_obj.MechanicName

            services = []
            for obj in ser_obj:
                service = {}
                service['description'] = obj.ServiceItem
                service['is_availed'] = obj.IsAvailed
                service['id'] = obj.id
                services.append(service)
            details['services'] = services

            total_parts_cost = 0.0
            total_taxable_price = 0.0
            optaxableprice = 0.0
            if spares_obj:
                spares = []
                for obj in spares_obj:
                    spare = {}
                    spare['description'] = obj.Description
                    spare['unit_price'] = obj.UnitPrice
                    spare['quantity'] = obj.Qty
                    spare['total_price'] = obj.TotalPrice
                    total_parts_cost += float(spare['total_price'])
                    spare['id'] = obj.id
                    spare['tax'] = "%.2f"%(config.TAX_PERCENTAGE)
                    spare['taxable_price'] = float(spare['total_price']) + (float(spare['total_price'])*(float(config.TAX_PERCENTAGE)/100))
                    total_taxable_price += float(spare['taxable_price'])
                    spare['identifier'] = obj.PartIdentifier
                    spares.append(spare)
                details['spares'] = spares

            if lab_cost_obj:
                details['lab_cost'] = "%.2f"%float(lab_cost_obj.LabourCharge)
                service_tax_amt = float(lab_cost_obj.LabourCharge)*(float(config.SERVICE_TAX_PERCENTAGE)/100)
                details['lab_cost_with_tax'] = "%.2f"%((float(lab_cost_obj.LabourCharge) + service_tax_amt))
            else:
                details['lab_cost'] = 0.0
                service_tax_amt = 0.0
                details['lab_cost_with_tax'] = 0.0

            if other_parts:
                details['otherparts'] = other_parts.OtherPartsDesc
                details['othercost'] = "%.2f"%float(other_parts.OtherPartsCost)
            else:
                details['otherparts'] = ""
                details['othercost'] = 0.0

            details['optax'] = "%.2f"%(config.TAX_PERCENTAGE)
            details['optaxableprice'] = float(details['othercost']) + (float(details['othercost'])*(float(config.TAX_PERCENTAGE)/100))

            
            
            details['total_parts_cost'] = "%.2f"%(total_parts_cost)
            details['total_parts_cost_editjc'] = "%.2f"%(total_parts_cost+float(details['othercost']))

            if lab_cost_obj:
                details['total_cost_editjc'] = "%.2f"%(float(details['total_parts_cost_editjc'])+ float(lab_cost_obj.LabourCharge))
                details['total_cost'] = "%.2f"%(total_parts_cost + float(lab_cost_obj.LabourCharge))
            else:
                details['total_cost_editjc'] = "%.2f"%(float(details['total_parts_cost_editjc'])+ float(0))
                details['total_cost'] = "%.2f"%(total_parts_cost + float(0))

            details['total_taxable_price'] = "%.2f"%(float(total_taxable_price)+details['optaxableprice'])
            details['total_cost_with_tax'] = "%.2f"%(float(details['total_taxable_price']) + float(details['lab_cost_with_tax']))
            details['service_tax'] = "%.2f"%(config.SERVICE_TAX_PERCENTAGE)
            
            if recomd_obj:
                details['recommendedservices'] = (recomd_obj.ServiceItems).split('##')
            else:
                details['recommendedservices'] = []

            if invoice_details:
                details['inv_no'] = lab_cost_obj.InvoiceNumber
                details['pay_mode'] = lab_cost_obj.PaymentMode
                details['gen_date'] = lab_cost_obj.GeneratedTime
            result = {"status": "success", "jobcard_details": details}
        else:
            result = {"status": "failure", "msg": "No info on the Job Card."}
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "Something went wrong."}
    return result

def updateStockQty(identifier, quantity, dealerid):
    try:
        if quantity == 0:
            return ""
        else:
            inventory_obj = Inventory.objects.get(PartIdentifier__iexact = identifier, DealerID = dealerid)
            inventory_obj.AvailableQty = float(inventory_obj.AvailableQty) - float(quantity)
            if inventory_obj.AvailableQty < 0:
                return "%s of quantity %s is not available"%(identifier, quantity)
            inventory_obj.save()
            return ""
    except ObjectDoesNotExist:
        return ("%s not in inventory"%identifier)

def createJobCard(details, dealerid):
    try:
        if isinstance(details['services'], list) and isinstance(details['spares'], list):
            jc_id = "JC" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '_' + str(random.randint(111, 999))
            warnings = []
            for spare in details['spares']:
                # deduct from inventory
                response = updateStockQty(spare['identifier'], spare['qty'], dealerid)
                if response:
                    warnings.append(response)
            if warnings:
                return {'status': 'failure', 'msg': warnings}
            else:
                for spare in details['spares']:
                    inventory_obj = Inventory.objects.get(PartIdentifier__iexact = spare['identifier'], DealerID__iexact=dealerid)
                    unit_price = float(inventory_obj.MRP)
                    qty = float(spare['qty'])
                    total_price = "%.2f"%(( unit_price * qty ))
                    qty = "%.2f"%(qty)
                    JCStocksInfo.objects.create(PartIdentifier = spare['identifier'],
                                            Description = spare['description'],
                                            UnitPrice = unit_price,
                                            Qty = qty,
                                            TotalPrice = total_price,
                                            JobCardID = jc_id,
                                            DealerID = dealerid)

                JCVehicleInfo.objects.create(VehicleNumber = details['veh_num'],
                                         Brand = details['brand'],
                                         Model = details['model'],
                                         FuelType = details['fuel_type'],
                                         ChassisNumber = details['c_num'],
                                         CustomerName = details['cust_name'],
                                         ContactNumber = details['cont_num'],
                                         Address = details['cont_address'],
                                         KilometersTicked = details['km_ticked'],
                                         JobCardID = jc_id,
                                         DealerID = dealerid,
                                         CreatedTime = str(datetime.datetime.now()))
                JCStatus.objects.create(JobCardID = jc_id,
                                    DealerID = dealerid,
                                    DeliveryTime = details['del_time'],
                                    MechanicName = details['mechanic_name'],
                                    Status = "OPEN",
                                    PendingReason = "",
                                    CreatedTime = str(datetime.datetime.now()),
                                    LastedEditedTime = str(datetime.datetime.now()),
                                    ServiceTypeId = details['ServiceTypeId'],
                                    )
                JCOtherStocksInfo.objects.create(OtherPartsDesc = details['otherparts_desc'],
                                            OtherPartsCost = details['otherparts_cost'],
                                            JobCardID = jc_id)
                for service in details['services']:
                    JCServiceDetails.objects.create(ServiceItem = service['description'],
                                                IsAvailed = service['is_availed'],
                                                JobCardID = jc_id,
                                                DealerID = dealerid)
                # update labour cost
                JCInvoiceAndLabourCost.objects.create(JobCardID = jc_id,
                                                  DealerID = dealerid,
                                                  InvoiceNumber = "",
                                                  LabourCharge = details['labour_cost'],
                                                  PaymentMode = "",
                                                  PartsTotalPrice = "",
                                                  VATPercentage = "",
                                                  TaxPercentage = "",
                                                  MechanicName = details['mechanic_name']
                                                  )

                service_items = "##".join(details['recommendedservices'])
                JCRecommendedServices.objects.create(JobCardID = jc_id,
                                                 DealerID = dealerid,
                                                 ServiceItems = service_items)

                result = {"status": "success", "msg": "Job Card created successfully", "jc_id": jc_id}
        else:
            raise
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "Something went wrong."}
    return result


def saveJobCard(details, dealerid, jc_id):
    try:
        jc_obj = JCStatus.objects.get(JobCardID__iexact = jc_id, DealerID__iexact = dealerid)
        other_parts = JCOtherStocksInfo.objects.get(JobCardID__iexact = jc_id)
        recomd_obj = JCRecommendedServices.objects.get(JobCardID__iexact = jc_id, DealerID__iexact = dealerid)
        if jc_obj.Status != 'CLOSED':
            if isinstance(details['services'], list) and isinstance(details['spares'], list):
                #veh_obj = JCVehicleInfo.objects.get(JobCardID__iexact = jc_id, DealerID__iexact = dealerid)
                #ser_obj = JCServiceDetails.objects.filter(JobCardID__iexact = jc_id, DealerID__iexact = dealerid)
                #spares_obj = JCStocksInfo.objects.filter(JobCardID__iexact = jc_id, DealerID__iexact = dealerid)
                warnings = []
                for spare in details['spares']:
                    inventory_obj = Inventory.objects.get(PartIdentifier__iexact = spare['identifier'], DealerID__iexact=dealerid)
                    try:
                        obj = JCStocksInfo.objects.get(id = int(spare['id']))
                        # deduct or update inventory
                        response = updateStockQty(spare['identifier'], float(spare['qty']) - float(obj.Qty), dealerid)
                        if response:
                            warnings.append(response)
                    except ObjectDoesNotExist:
                        # deduct from inventory
                        response = updateStockQty(spare['identifier'], spare['qty'], dealerid)
                        if response:
                            warnings.append(response)
                if warnings:
                    return {'status': 'failure', 'msg': warnings}
                else:
                    for spare in details['spares']:
                        inventory_obj = Inventory.objects.get(PartIdentifier__iexact = spare['identifier'], DealerID__iexact=dealerid)
                        try:
                            obj = JCStocksInfo.objects.get(id = int(spare['id']))
                            obj.Description = spare['description']
                            obj.UnitPrice = "%.2f"%float(inventory_obj.MRP)
                            obj.Qty = "%.2f"%float(spare['qty'])
                            obj.TotalPrice = "%.2f"%(( float(inventory_obj.MRP) * float(spare['qty']) ))
                            obj.save()
                        except ObjectDoesNotExist:
                            JCStocksInfo.objects.create(PartIdentifier = spare['identifier'],
                                            Description = spare['description'],
                                            UnitPrice = spare['unit_price'],
                                            Qty = spare['qty'],
                                            TotalPrice = spare['total_price'],
                                            JobCardID = jc_id,
                                            DealerID = dealerid)

                    #veh_obj.VehicleNumber = details['veh_num']
                    #veh_obj.Brand = details['brand']
                    #veh_obj.Model = details['model']
                    #veh_obj.FuelType = details['fuel_type']
                    #veh_obj.ChassisNumber = details['c_num']
                    #veh_obj.CustomerName = details['cust_name']
                    #veh_obj.ContactNumber = details['cont_num']
                    #veh_obj.Address = details['cont_address']
                    #veh_obj.KilometersTicked = details['km_ticked']
                    #veh_obj.JobCardID = details['jc_id']
                    #veh_obj.save()

                    jc_obj.DeliveryTime = details['del_time']
                    jc_obj.service_reminder_time = details['service_reminder_time']
                    jc_obj.Status = details['status']
                    jc_obj.PendingReason = details['reason']
                    jc_obj.ServiceTypeId = details['ServiceTypeId']
                    jc_obj.save()
                    
                    other_parts.OtherPartsDesc=details['otherparts_desc']
                    other_parts.OtherPartsCost=details['otherparts_cost']
                    other_parts.save()

                    for service in details['services']:
                        try:
                            obj = JCServiceDetails.objects.get(id = int(service['id']))
                            obj.ServiceItem = service['description']
                            obj.IsAvailed = service['is_availed']
                            obj.save()
                        except ObjectDoesNotExist:
                            JCServiceDetails.objects.create(ServiceItem = service['description'],
                                                IsAvailed = service['is_availed'],
                                                JobCardID = jc_id,
                                                DealerID = dealerid)

                    # update labour cost
                    try:
                        jc_inv_obj = JCInvoiceAndLabourCost.objects.get(JobCardID__iexact = jc_id, DealerID__iexact = dealerid)
                        jc_inv_obj.LabourCharge = details['labour_cost']
                        jc_inv_obj.save()
                    except ObjectDoesNotExist:
                        JCInvoiceAndLabourCost.objects.create(JobCardID = jc_id,
                                                          DealerID = dealerid,
                                                          InvoiceNumber = "",
                                                          LabourCharge = details['labour_cost'],
                                                          PaymentMode = "",
                                                          PartsTotalPrice = "",
                                                          VATPercentage = "",
                                                          TaxPercentage = "",
                                                          MechanicName=details['mechanic_name']
                                                          )

                    recomd_obj.ServiceItems = "##".join(details['recommendedservices'])
                    recomd_obj.save()

                    result = {"status": "success", "msg": "Saved successfully"}
            else:
                raise
        else:
            result = {"status": "failure", "msg": "Operation not permitted"}
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "Something went wrong."}
    return result


def generateInvoice(jc_id, pmt_mode, dealerid):
    try:
        status_obj = JCStatus.objects.get(JobCardID__iexact = jc_id, DealerID__iexact = dealerid)
        if status_obj.Status == "CLOSED":
            invoice_obj = JCInvoiceAndLabourCost.objects.get(JobCardID__iexact = jc_id, DealerID__iexact = dealerid)
            if invoice_obj.InvoiceNumber == "":
                spares_obj = JCStocksInfo.objects.filter(JobCardID__iexact = jc_id, DealerID__iexact = dealerid)
                other_parts_inv = other_parts = JCOtherStocksInfo.objects.get(JobCardID__iexact = jc_id)
                total_parts_cost = 0.00
                if spares_obj:
                    for obj in spares_obj:
                        total_parts_cost += float(obj.TotalPrice)
                invoice_number = "INV" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '_' + str(random.randint(111, 999))
                invoice_obj.InvoiceNumber = invoice_number
                invoice_obj.PaymentMode = pmt_mode
                invoice_obj.PartsTotalPrice = "%.2f"%total_parts_cost
                invoice_obj.VATPercentage = "%.2f"%config.TAX_PERCENTAGE
                invoice_obj.TaxPercentage = "%.2f"%config.SERVICE_TAX_PERCENTAGE
                invoice_obj.GeneratedTime = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
                invoice_obj.save()
                result = {"status": "success", "msg": "Invoice generated successfully"}
            else:
                result = {"status": "failure", "msg": "Invoice already generated"}
        else:
            result = {"status": "failure", "msg": "Job card is not closed"}
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "Something went wrong."}
    return result


def fetchServiceHistory(veh_num, c_num):
    try:
        history = []
        if veh_num:
            objs = JCVehicleInfo.objects.filter(VehicleNumber__iexact = veh_num)
        elif c_num:
            objs = JCVehicleInfo.objects.filter(ChassisNumber__iexact = c_num)
        job_card_km_map = []
        for obj in objs:
            temp_dict = {}
            temp_dict['km'] = obj.KilometersTicked
            temp_dict['jc_id'] = obj.JobCardID
            temp_dict['date'] = obj.CreatedTime[:10]
            job_card_km_map.append(temp_dict)
        for temp_dict in job_card_km_map:
            objs = JCServiceDetails .objects.filter(JobCardID__iexact = temp_dict['jc_id'])
            services = []
            for obj in objs:
                temp_dict2 = {}
                temp_dict2['service_item'] = obj.ServiceItem
                temp_dict2['is_availed'] = obj.IsAvailed
                services.append(temp_dict2)
            temp_dict['services'] = services
            history.append(temp_dict)
        result = {"status": "success", "history": history}
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "Something went wrong."}
    return result


def getDashboardData(dealerid):
    try:
        result = {}
        result['open_jc'] = JCStatus.objects.filter(DealerID__iexact = dealerid, Status__iexact = "OPEN").count()
        open_old = JCStatus.objects.filter(DealerID__iexact = dealerid, Status__iexact = "OPEN", CreatedTime__lte = str(datetime.date.today())).count()
        pending_old = JCStatus.objects.filter(DealerID__iexact = dealerid, Status__iexact = "PENDING", CreatedTime__lte = str(datetime.date.today())).count()
        result['pending_jc'] = open_old + pending_old
        result['to_deliever_today'] = JCStatus.objects.filter(DealerID__iexact = dealerid, DeliveryTime__iexact = str(datetime.date.today())).count()
        objects = Inventory.objects.filter(DealerID__iexact = dealerid)
        result['min_order'] = 0
        for obj in objects:
            if float(obj.AvailableQty) <= float(obj.MinQty):
                result['min_order'] = result['min_order'] + 1
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "Something went wrong."}
    return result


def fetchInventoryData(dealerid):
    try:
        objects = Inventory.objects.filter(DealerID__iexact = dealerid)
        data = []
        result = {"status": "failure", "msg": "No stocks in inventory."}
        for obj in objects:
            temp_dict = {}
            temp_dict['brand'] = obj.Brand
            temp_dict['model'] = obj.Model
            temp_dict['identifier'] = obj.PartIdentifier
            temp_dict['description'] = obj.Description
            temp_dict['min_qty'] = obj.MinQty
            temp_dict['avail_qty'] = obj.AvailableQty
            temp_dict['NDP'] = obj.NDP
            temp_dict['MRP'] = obj.MRP
            temp_dict['critical'] = obj.IsCritical
            temp_dict['alternate'] = obj.AlternatePart
            data.append(temp_dict)
            result = {"status": "success", "data": data}
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "Something went wrong."}
    return result


def updateInventoryStocks(details, dealerid):
    try:
        if isinstance(eval(details), list):
            for detail in details:
                try:
                    obj = Inventory.objects.get(DealerID__iexact = dealerid, PartIdentifier__iexact = detail['identifier'])
                    obj.Brand = detail['brand']
                    obj.Model = detail['model']
                    obj.Description = detail['description']
                    obj.MinQty = detail['min_qty']
                    obj.AvailableQty = float(obj.AvailableQty) + float(detail['avail_qty'])
                    obj.NDP = detail['NDP']
                    obj.MRP = detail['MRP']
                    obj.IsCritical = detail['critical']
                    obj.AlternatePart = detail['alternate']
                    obj.save()
                except ObjectDoesNotExist:
                    Inventory.objects.create(DealerID = dealerid,
                                             Brand = detail['brand'],
                                             Model = detail['model'],
                                             PartIdentifier = detail['identifier'],
                                             Description = detail['description'],
                                             MinQty = detail['min_qty'],
                                             AvailableQty = detail['avail_qty'],
                                             NDP = detail['NDP'],
                                             MRP = detail['MRP'],
                                             IsCritical = detail['critical'],
                                             AlternatePart = detail['alternate'])
            result = {"status": "success", "msg": "updated successfully"}
        else:
            raise
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "Something went wrong."}
    return result

def updateInventoryItem(detail, dealerid):
    try:
            try:
                obj = Inventory.objects.get(DealerID__iexact = dealerid, PartIdentifier__iexact = detail['identifier'])
                obj.Brand = detail['brand']
                obj.Model = detail['model']
                obj.Description = detail['description']
                obj.MinQty = detail['min_qty']
                obj.AvailableQty = detail['avail_qty']
                obj.NDP = detail['ndp']
                obj.MRP = detail['mrp']
                obj.IsCritical = detail['critical']
                obj.AlternatePart = detail['alternate']
                obj.save()
                result = {"status": "success", "msg": "updated successfully"}
            except ObjectDoesNotExist:
                result = {"status": "failure", "msg": "The item is not in inventory."}
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "Something went wrong."}
    return result

def getInventoryData(identifier, dealerid):
    try:
        obj = Inventory.objects.get(DealerID__iexact = dealerid, PartIdentifier__iexact = identifier)
        temp_dict = {}
        temp_dict['brand'] = obj.Brand
        temp_dict['model'] = obj.Model
        temp_dict['identifier'] = obj.PartIdentifier
        temp_dict['description'] = obj.Description
        temp_dict['min_qty'] = obj.MinQty
        temp_dict['avail_qty'] = obj.AvailableQty
        temp_dict['NDP'] = obj.NDP
        temp_dict['MRP'] = obj.MRP
        if obj.IsCritical == '1':
            temp_dict['critical'] = True
        else:
            temp_dict['critical'] = False
        temp_dict['alternate'] = obj.AlternatePart
        return temp_dict
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
    return {}


def getJobCardsList(dealerid, for_invoice=False):
    try:
        result = []
        jc_objs = JCStatus.objects.filter(DealerID__iexact = dealerid)

        if jc_objs:
            for obj in jc_objs:
                try:
                    if for_invoice or ((obj.CreatedTime[:10] < str(datetime.datetime.now())[:10] and obj.Status !="CLOSED") or obj.CreatedTime[:10] == str(datetime.datetime.now())[:10]):
                        veh_obj = JCVehicleInfo.objects.get(JobCardID = obj.JobCardID, DealerID = dealerid)
                        if veh_obj:
                            temp_dict = {}
                            temp_dict['jc_id'] = obj.JobCardID
                            temp_dict['veh_no'] = veh_obj.VehicleNumber
                            temp_dict['model'] = veh_obj.Brand + " " + veh_obj.Model
                            temp_dict['status'] = obj.Status
                            temp_dict['service_type'] = "%s - %s" % (global_constants.service_types[obj.ServiceTypeId]['service_type'],
                                global_constants.service_types[obj.ServiceTypeId]['classification'])
                            temp_dict['invoice'] = False
                            temp_dict['mechanic_name'] = obj.MechanicName
                            try:
                                invoice_obj = JCInvoiceAndLabourCost.objects.get(JobCardID__iexact = obj.JobCardID)
                            except JCInvoiceAndLabourCost.DoesNotExist:
                                invoice_obj = None

                            if invoice_obj and invoice_obj.InvoiceNumber != "":
                                temp_dict['invoice'] = True
                                temp_dict['mode'] = invoice_obj.PaymentMode
                            result.append(temp_dict)
                except:
                    error_logger = log_rotator.error_logger()
                    error_logger.debug("Exception::", exc_info=True)
                    continue
        return result
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
    return []

def getCompliantCodes():
    try:
        compliants = list(ComplaintCode.objects.all())
        data = []
        if compliants:
            for compliant in compliants:
                temp_dict = {}
                temp_dict['Code'] = compliant.Code
                temp_dict['Description'] = compliant.Description
                temp_dict['Aggregate'] = compliant.Aggregate
                data.append(temp_dict)
        result = {"status": "success", "compliants": data}
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {"status": "failure", "msg": "Something went wrong."}
    return result

def getCarBrands():
    try:
        brands = list(SupportedCarBrands.objects.all())
        data = []
        if brands:
            for brand in brands:
                data.append(brand)
        result = {'brands' : data}
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        result = {'brands' : []}
    return result
#------


def save_image(image_id, image):
    try:
        db = MySQLdb.connect("localhost", "root", settings.DATABASES['default']['PASSWORD'], "easedb" )
        query = "INSERT INTO images values ('"+image_id+"', '"+image+"')"
        cursor=db.cursor()
        cursor.execute(query)
        db.commit()
        db.close()
        return True
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        return False


def get_image():
    try:
        db = MySQLdb.connect("localhost", "root", settings.DATABASES['default']['PASSWORD'], "easedb" )
        query = "SELECT image FROM images limit 1"
        cursor=db.cursor()
        cursor.execute(query)
        image = cursor.fetchall()[0]
        db.close()
        return image
    except:
        error_logger = log_rotator.error_logger()
        error_logger.debug("Exception::", exc_info=True)
        return False


def vehicle_number_check(reg_data):

    reg_data = reg_data.split(' ')

    if len(reg_data) == 3:
        if (
            not reg_data[0].isalpha() or
            len(reg_data[0]) != 2 or
            not reg_data[1].isdigit() or
            len(reg_data[1]) != 2 or
            not reg_data[2].isdigit() or
            len(reg_data[2]) != 4
            ):
            return False, "Invalid Registration Number Format."

    else:
        if (
            not reg_data[0].isalpha() or
            len(reg_data[0]) != 2 or
            not reg_data[1].isdigit() or
            len(reg_data[1]) != 2 or
            not reg_data[2].isalpha() or
            len(reg_data[2]) > 3 or
            not reg_data[3].isdigit() or
            len(reg_data[3]) != 4
            ):
            return False, "Invalid Registration Number Format."

    return True, None