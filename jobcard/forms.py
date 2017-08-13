from django import forms

class BookServiceForm(forms.Form):
    
    vehicle_type = forms.CharField()
    vehicle_model_id = forms.CharField()
    vehicle_registration_number = forms.CharField()
    service_center_id = forms.CharField()
    customer_address_id = forms.CharField()
    service_details = forms.CharField()


class RetrieveServiceForm(forms.Form):
    
    booking_id = forms.CharField()