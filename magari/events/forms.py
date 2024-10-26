from django import forms
from .models import Event
from .models import CarGroup

class EventForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'time', 'location', 'registration_fee', 'group']

class EventRegistrationForm(forms.Form):
    confirm_registration = forms.BooleanField(label="I confirm my registration", required=True)


class CarGroupForm(forms.ModelForm):
    class Meta:
        model = CarGroup
        fields = ['name', 'description']