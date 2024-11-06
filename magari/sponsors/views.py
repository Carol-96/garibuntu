from django.shortcuts import render,redirect, get_object_or_404
from .models import Sponsor
from .forms import SponsorRegistrationForm, SponsorLoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Announcement
from events.models import Event
from django.contrib.auth import get_user_model
from .decorators import sponsor_required

# Access the user model dynamically
User = get_user_model()


def sponsor_list(request):
    sponsors = Sponsor.objects.all()
    return render(request, 'sponsor_list.html', {'sponsors':sponsors})


# Sponsor Registration View
def sponsor_register(request):
    if request.method == 'POST':
        form = SponsorRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect('sponsors:sponsor_login')  # Adjust to your sponsor login URL
    else:
        form = SponsorRegistrationForm()
    return render(request, 'sponsor_reg.html', {'form': form})



def sponsor_login(request):
    if request.method == 'POST':
        form = SponsorLoginForm(request.POST)
        if form.is_valid():
            company_name = form.cleaned_data['company_name']
            password = form.cleaned_data['password']
            try:
                sponsor = Sponsor.objects.get(company_name=company_name)
                if sponsor.check_password(password):
                    request.session['sponsor_id'] = sponsor.id  # Custom session for sponsor login
                    messages.success(request, "You are now logged in.")
                    return redirect('sponsors:sponsor_dashboard')  # Redirect to sponsor dashboard
                else:
                    messages.error(request, "Invalid password.")
            except Sponsor.DoesNotExist:
                messages.error(request, "Invalid company name.")
    else:
        form = SponsorLoginForm()
    return render(request, 'sponsor_login.html', {'form': form})

def sponsor_logout(request):
    logout(request)
    request.session.pop('sponsor_id', None)
    messages.success(request, "You have been logged out.")
    return redirect('sponsor_login')


@sponsor_required
def sponsor_dashboard(request):
    # Fetch the sponsor's information and sponsored events
    user = request.user

    # Retrieve the events sponsored by the logged-in user
    # sponsored_events = Event.objects.filter(sponsor=user.sponsorprofile).order_by('-date')

    # Retrieve announcements for display
    # announcements = Announcement.objects.all().order_by('-date')[:5]  # Limit to the latest 5 announcements

    context = {
        'user': user,
        #'sponsored_events': sponsored_events,
        #'announcements': announcements,
    }
    
    return render(request, 'sponsor_dashboard.html', context)
