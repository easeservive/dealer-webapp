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