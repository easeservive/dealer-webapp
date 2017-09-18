from django import forms

class RegisterForm(forms.Form):
    
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    mobile = forms.IntegerField()
    password = forms.CharField()
    address = forms.CharField(required=False)


class LoginForm(forms.Form):
    
    mobile = forms.IntegerField()
    password = forms.CharField()


class OtpForm(forms.Form):
    
    otp_value = forms.CharField()
    otptranid = forms.CharField()


class ResendOtpForm(forms.Form):

    mobile = forms.IntegerField()


class AddAddressForm(forms.Form):

    address_line_1 = forms.CharField()
    address_line_2 = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    zipcode = forms.IntegerField()


class BookServiceForm(forms.Form):

    vehicle_type = forms.CharField()
    vehicle_model_id = forms.CharField()
    vehicle_registration_number = forms.CharField()
    service_center_id = forms.CharField()
    customer_address_id = forms.CharField()
    service_details = forms.CharField()


class AddVehicleForm(forms.Form):

    vehicle_model_id = forms.CharField()
    vehicle_registration_number = forms.CharField()
    fuel_type = forms.CharField()
    total_kms = forms.IntegerField()
    year = forms.IntegerField()
    chassis_number = forms.CharField(required=False)


class TipsForm(forms.Form):

    vehicle_type = forms.CharField()


class RemoveUserForm(forms.Form):

    mobile = forms.IntegerField()
    api_key = forms.CharField()