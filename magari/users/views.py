from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.


def profile(request):
    return render(request, 'users/profile.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})

def profile(request):
    return render(request, 'users/profile.html')

class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = AuthenticationForm  # Use class, not an instance
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')