from django import forms

class RetrieveServiceCenter(forms.Form):

    service_center_id = forms.IntegerField()