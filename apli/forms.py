from django.contrib.auth.models import User
from django import forms
from .models import Client
from .validators import clean_email
from django.contrib.auth import get_user_model #regsitration

User = get_user_model()




#crear un nuevo cliente isma ABRE
class ClientCreateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'nombre_completo',
            'company',
            'nickname',
            'company_short',
            'pais_address',
            'ciudad_address',
            'codigo_address',
            'street_address',
            'numero_address',
            'email',
            'telephone',
            'comment',
        ]


    def clean_name(self):
        nombre_completo = self.cleaned_data.get("nombre_completo")
        if nombre_completo == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name
#crear un nuevo cliente isma CIERRE

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'nombre_completo',
            'nickname',
            'company',
            'company_short',
            'pais_address',
            'ciudad_address',
            'codigo_address',
            'street_address',
            'numero_address',
            'email',
            'telephone',
            'comment'
        ]


















