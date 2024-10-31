from django import forms
from .models import Event, CarGroup, EventRegistration

class EventForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'time', 'location', 'registration_fee', 'group', 'poster']

class EventRegistrationForm(forms.ModelForm):


    class Meta:
        model = EventRegistration
        fields = ['registration_type', 'payment_confirmation_code']  # Include other relevant fields here
        widgets = {
            'registration_type': forms.Select(choices=[
                ('sponsor', 'Sponsor'),
                ('friend', 'Friend of Car Group'),
                ('member', 'Car Group Member'),
            ]),
            'payment_confirmation_code': forms.TextInput(attrs={'placeholder': 'Enter confirmation code'}),
        }

    def clean_payment_confirmation_code(self):
        # Example validation for payment_confirmation_code
        code = self.cleaned_data.get('payment_confirmation_code')
        if code and len(code) < 5:  # Just an example check
            raise forms.ValidationError("Confirmation code must be at least 5 characters.")
        return code


class CarGroupForm(forms.ModelForm):
    class Meta:
        model = CarGroup
        fields = ['name', 'description']