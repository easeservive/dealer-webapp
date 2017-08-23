from django import forms

class BookServiceForm(forms.Form):
    
    vehicle_type = forms.CharField()
    vehicle_model_id = forms.IntegerField()
    vehicle_registration_number = forms.CharField()
    service_center_id = forms.CharField()
    customer_address_id = forms.CharField()
    service_details = forms.CharField()


class RetrieveServiceForm(forms.Form):
    
    booking_id = forms.IntegerField()


class ServiceFeedbackForm(forms.Form):
    
    booking_id = forms.IntegerField()
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

    booking_id = forms.IntegerField()