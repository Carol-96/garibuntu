from django.urls import path
from . import views


urlpatterns = [
    path('', views.sponsor_list, name='sponsor_list')
]