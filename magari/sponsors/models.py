from django.db import models

# Create your models here.

class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='sponsors/', blank=True, null=True)
    website_url = models.CharField(max_length=200, blank=True, null=True)
    sponsor_type = models.CharField(max_length=100, choices=[('Gold', 'Gold'), ('Silver', 'Silver'), ('Bronze', 'Bronze')])

    def __str__(self):
        return self.name
    