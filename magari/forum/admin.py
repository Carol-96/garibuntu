from django.contrib import admin
from .models import ForumThread, ForumPost, ForumReply

# Register your models here.
admin.site.register(ForumThread)
admin.site.register(ForumPost)
admin.site.register(ForumReply)