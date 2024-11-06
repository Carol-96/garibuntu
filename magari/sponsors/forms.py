from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Sponsor
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model 
from django import forms
from .models import Sponsor
from django.contrib.auth.hashers import make_password


User = get_user_model()


class SponsorRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
        label="Password"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        label="Confirm Password"
    )

    class Meta:
        model = Sponsor
        fields = ['company_name', 'contact_person', 'email', 'phone_number', 'logo', 'website_url']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        
        return cleaned_data

    def save(self, commit=True):
        sponsor = super().save(commit=False)
        sponsor.password = make_password(self.cleaned_data["password1"])  # Set hashed password
        if commit:
            sponsor.save()
        return sponsor




class SponsorLoginForm(forms.Form):
    company_name = forms.CharField(label="Company Name")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")