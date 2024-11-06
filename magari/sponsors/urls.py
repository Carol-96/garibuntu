from django.urls import path
from . import views

app_name='sponsors'

urlpatterns = [
    path('', views.sponsor_list, name='sponsor_list'),
    path('register/', views.sponsor_register, name='sponsor_register'),
    path('sponsors-login/', views.sponsor_login, name='sponsor_login'),
    path('sponsors-dashboard/', views.sponsor_dashboard, name='sponsor_dashboard'),
    
]