from django import forms
from .models import Sponsor


class SponsorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = ["company_name", "contact_person", "email", "phone_number", "logo", "website_url"]

