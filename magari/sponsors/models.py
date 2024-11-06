from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
    
class Sponsor(models.Model):
    company_name = models.CharField(max_length=255, unique=True)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='sponsor_logos/', blank=True, null=True)
    website_url = models.URLField(blank=True, null=True)
    password = models.CharField(max_length=128)  # Stores hashed password

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.company_name



class Announcement(models.Model):
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Announcement on {self.date.strftime('%Y-%m-%d')}"