from django.urls import path
from . import views
app_name = 'forum'
urlpatterns = [
    path('', views.thread_list, name='thread_list'),
    path('thread/<int:thread_id>/', views.thread_detail, name='thread_detail'),
    path('thread/new/', views.create_thread, name='create_thread'),
    # path('thread/<int:thread_id>/post/', views.create_post, name='create_post'),
    #path('post/<int:post_id>/reply/', views.create_reply, name='create_reply'),
]