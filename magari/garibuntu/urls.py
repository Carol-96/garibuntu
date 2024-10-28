from django.urls import path, include
from . import views
app_name = 'garibuntu'
urlpatterns = [
    path('', views.home, name='home'),
    path('users/', include('users.urls', namespace='users')), 
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cargroupslist/', views.car_group_list, name='car_group_list'), 
    path('car-groups/<int:group_id>/', views.car_group_detail, name='car_group_detail'),
]