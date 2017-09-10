from django import forms

class RetrieveServiceCenter(forms.Form):

    service_center_id = forms.IntegerField()

class RetrieveVehicleReview(forms.Form):

    vehicle_model_id = forms.IntegerField()

class RetrieveVehicleModels(forms.Form):

    vehicle_type = forms.CharField()