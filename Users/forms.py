from django.forms.extras.widgets import SelectDateWidget
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from Users.models import User,Usuario
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

	class Meta:
		model = Usuario
		fields = ['username', 'email']		
		

class EditarEmailForm(forms.Form):

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        """Obtener request"""
        self.request = kwargs.pop('request')
        return super(EditarEmailForm, self).__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data['email']
        # Comprobar si ha cambiado el email
        actual_email = self.request.user.email
        username = self.request.user.username
        if email != actual_email:
            # Si lo ha cambiado, comprobar que no exista en la db.
            # Exluye el usuario actual.
            existe = User.objects.filter(email=email).exclude(username=username)
            if existe:
                raise forms.ValidationError('Ya existe un email igual en la db.')
        return email


class EditarNombreForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
