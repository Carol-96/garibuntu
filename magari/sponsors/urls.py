from django.urls import path
from . import views

app_name='sponsors'

urlpatterns = [
    path('', views.sponsor_list, name='sponsor_list'),
    path('register-sponsor/', views.register_sponsor, name='register_sponsor')
]