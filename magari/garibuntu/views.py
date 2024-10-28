from django.shortcuts import render, HttpResponse, get_object_or_404
from events.models import CarGroup


# Create your views here.

def home(request):
    return render(request, 'index.html')

def dashboard(request):
    user = request.user
    return render(request, 'dashboard.html', {'user':user})

def car_group_list(request):
    groups = CarGroup.objects.all()
    return render(request, 'car-groups-list.html', {'groups':groups})


def car_group_detail(request, group_id):
    car_group = get_object_or_404(CarGroup, pk=group_id)
    return render(request, 'car_group_detail.html', {'car_group': car_group})