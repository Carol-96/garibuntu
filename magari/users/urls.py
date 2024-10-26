from django.urls import path
from . import views
from .views import CustomLoginView


urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', CustomLoginView.as_view(), name='login')
]