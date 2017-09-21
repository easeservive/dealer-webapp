from django import forms

class BookServiceForm(forms.Form):
    
    #vehicle_type = forms.CharField()
    vehicle_model_id = forms.CharField()
    vehicle_registration_number = forms.CharField()
    service_center_id = forms.CharField()
    customer_address_id = forms.CharField()
    service_details = forms.CharField()
    service_type_id = forms.CharField()


class RetrieveServiceForm(forms.Form):
    
    booking_id = forms.CharField()


class ServiceFeedbackForm(forms.Form):
    
    booking_id = forms.CharField()
    feedback_text = forms.CharField(required=False)
    feedback_stars = forms.IntegerField()


class BookEmergencyServiceForm(forms.Form):
    
    vehicle_type = forms.CharField()
    customer_address_id = forms.CharField(required=False)
    customer_latlon = forms.CharField(required=False)
    service_details = forms.CharField()


class RetrieveServiceRequests(forms.Form):

    service_center_id = forms.CharField()


class AcceptServiceForm(forms.Form):

    booking_id = forms.CharField()
    #booking_type = forms.CharField()


class JcForm(forms.Form):

    veh_num = forms.CharField()
    brand = forms.CharField()
    model = forms.CharField()
    fuel_type = forms.CharField()
    c_num = forms.CharField(required=False)
    cust_name = forms.CharField()
    cont_num = forms.IntegerField()
    cont_address = forms.CharField()
    km_ticked = forms.IntegerField()
    del_time = forms.CharField()
    status = forms.CharField()
    reason = forms.CharField()
    mechanic_name = forms.CharField()
    services = forms.CharField(required=False)
    spares = forms.CharField(required=False)
    otherparts_desc = forms.CharField(required=False)
    otherparts_cost = forms.CharField(required=False)
    recommendedservices = forms.CharField(required=False)
    labour_cost = forms.CharField(required=False)
    service_type_id = forms.CharField()


class SaveJcForm(forms.Form):

    veh_num = forms.CharField()
    brand = forms.CharField()
    model = forms.CharField()
    fuel_type = forms.CharField()
    c_num = forms.CharField(required=False)
    cust_name = forms.CharField()
    cont_num = forms.IntegerField()
    cont_address = forms.CharField()
    km_ticked = forms.IntegerField()
    del_time = forms.CharField()
    status = forms.CharField()
    reason = forms.CharField()
    mechanic_name = forms.CharField()
    services = forms.CharField(required=False)
    spares = forms.CharField(required=False)
    otherparts_desc = forms.CharField(required=False)
    otherparts_cost = forms.CharField(required=False)
    recommendedservices = forms.CharField(required=False)
    labour_cost = forms.CharField(required=False)
    jc_id = forms.CharField()
    service_reminder_time = forms.CharField(required=False)
    service_type_id = forms.CharField()


class RetrieveVehicleDataForm(forms.Form):

    vehicle_registration_number = forms.CharField()