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


class ServiceFeedbackForm(forms.Form):
    
    booking_id = forms.CharField()
    feedback_text = forms.CharField(required=False)
    feedback_stars = forms.IntegerField()


class BookEmergencyServiceForm(forms.Form):
    
    vehicle_type = forms.CharField()
    customer_address_id = forms.CharField(required=False)
    customer_latlon = forms.CharField(required=False)
    service_details = forms.CharField()