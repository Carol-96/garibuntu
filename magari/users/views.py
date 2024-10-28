from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, LoginForm
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
            return redirect('users:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm  # Use the custom form
    redirect_authenticated_user = False

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)  # Session expires on browser close
        else:
            self.request.session.set_expiry(1209600)  # Session expires in 2 weeks
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('dashboard')
    
   