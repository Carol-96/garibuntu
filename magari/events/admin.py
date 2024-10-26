from django.contrib import admin
from .models import CarGroup, Event, EventRegistration

# Register your models here.

admin.site.register(CarGroup)
admin.site.register(Event)
admin.site.register(EventRegistration)
