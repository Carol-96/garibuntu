from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, EventRegistration
from django.contrib.auth.decorators import login_required
from .forms import EventForm, CarGroupForm, EventRegistrationForm


# Create your views here.

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events':events})


def register_for_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    form = EventRegistrationForm()
    if request.method == 'POST':
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    
    return render(request, 'event_register.html', {'event':event, 'form':form})


@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'event_form.html', {'form': form})  



@login_required
def create_car_group(request):
    if request.method == 'POST':
        form = CarGroupForm(request.POST)
        if form.is_valid():
            car_group = form.save(commit=False)
            car_group.created_by = request.user
            car_group.save()
            return redirect('car_group_list')
    else:
        form = CarGroupForm()
    return render(request, 'car_group_form.html', {'form': form})
