from django.db import models

# Create your models here.

class Sponsor(models.Model):
    company_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='sponsors/', blank=True, null=True)
    website_url = models.CharField(max_length=200, blank=True, null=True)
    contact_person = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField()
    
    def __str__(self):
        return self.company_name
    