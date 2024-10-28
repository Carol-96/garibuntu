from django.shortcuts import render
from .models import Sponsor

# Create your views here.


def sponsor_list(request):
    sponsors = Sponsor.objects.all()
    return render(request, 'sponsor_list.html', {'sponsors':sponsors})


