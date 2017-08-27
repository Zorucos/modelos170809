from django.contrib.auth.models import User
from django import forms
from .models import Client, Person, Assignment, Horaire, Cost, Attachment, Project
from .validators import clean_email
from django.contrib.auth import get_user_model #regsitration


User = get_user_model()
# new task


# crear un nuevo cliente isma ABRE
class ClientCreateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'name',
            'name_short',
            'company',
            'company_short',
            'country',
            'city',
            'zip_code',
            'address',
            'email',
            'phone',
            'comment',
        ]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name
# crear un nuevo cliente isma CIERRE


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'name',
            'name_short',
            'company',
            'company_short',
            'country',
            'city',
            'zip_code',
            'address',
            'email',
            'phone',
            'comment',
        ]

# crear un nuevo Person isma ABRE
class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            'name',
            'name_short',
            'company',
            'company_short',
            'agent',
            'agent_short',
            'country',
            'city',
            'zip_code',
            'address',
            'email',
            'phone',
            'comment',
            'sedcard',
            'statut',
            'bank_account',
            'website',
        ]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name
