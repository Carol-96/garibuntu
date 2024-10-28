from django.db import models
from users.models import User
from django.utils import timezone

# Create your models here.

class CarGroup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_groups')
    members = models.ManyToManyField(User, related_name='joined_groups')

    def __str__(self):
        return self.name 
    

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    registration_fee = models.DecimalField(max_digits=10, decimal_places=2)
    group = models.ForeignKey(CarGroup, on_delete=models.CASCADE, related_name='events')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_events')
    attendees = models.ManyToManyField(User, through='EventRegistration', related_name='events')


    def __str__(self):
        return f"{self.title} - {self.date}"
    
class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} registered for {self.event.title}"