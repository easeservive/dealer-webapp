from django.shortcuts import render
from django.contrib.auth.models import User
from . import forms
from . import models


def register(request):

	if request.method == 'GET':
		# if user is logged in redirect him to home page
        if request.user.is_authenticated():
            return HttpResponseRedirect('home', reason="User Alerady Logged In")
        # if not send registration page
		else:
            return render(request, "account/registration.html")

    register_form = forms.RegisterForm(request.data)
    if register_form.is_valid():

        try:
            user_obj = User.objects.create_user(
                username = register_form.cleaned_data['mobile'],
                email = register_form.cleaned_data['email'],
                password = register_form.cleaned_data['password'],
                last_login = timezone.now()
            )

            customer_obj = models.models.objects.create(
                mobile = register_form.cleaned_data['mobile'],
                first_name = register_form.cleaned_data['first_name'],
                last_name = register_form.cleaned_data['last_name'],
                address = register_form.cleaned_data['address']
            )

        except IntegrityError:
            error_logger = log_rotator.error_logger()
            error_logger.debug("Exception::", exc_info=True)
            return Response({'status': "failure", 'msg': "User account already exists."}, status=status_code.HTTP_409_CONFLICT)

    else:
        form = NameForm()
        return render(request, 'registration.html', {'form': form})
    
    return Response({'status': "success", 'msg': "Account creation successful.", 'otptranid': otptranid})