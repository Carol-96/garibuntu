from django.shortcuts import render,redirect
from .models import Sponsor
from .forms import SponsorRegistrationForm

# Create your views here.


def sponsor_list(request):
    sponsors = Sponsor.objects.all()
    return render(request, 'sponsor_list.html', {'sponsors':sponsors})


def register_sponsor(request):
    form = SponsorRegistrationForm()
    if request.method == 'POST':
        form = SponsorRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    return render(request, "sponsor_reg.html",{"form":form})


