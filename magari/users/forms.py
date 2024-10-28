from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    profile_picture = forms.ImageField(required=False)
    bio = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'profile_picture', 'bio']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'profile_picture', 'bio']


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'autocomplete': 'username',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'autocomplete': 'current-password',
        })
    )
    remember_me = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label="Remember Me"
    )