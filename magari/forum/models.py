from django.conf import settings
from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone

class ForumThread(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='threads')
    created_at = models.DateTimeField(auto_now_add=True)
    is_locked = models.BooleanField(default=False)  # New field to lock threads
    is_deleted = models.BooleanField(default=False)  # Soft delete for threads

    class Meta:
        permissions = [
            ('can_lock_thread', 'Can lock threads'),
            ('can_delete_thread', 'Can delete threads'),
            ('can_create_thread', 'Can create threads'),
        ]
    
    def __str__(self):
        return self.title

class ForumPost(models.Model):
    thread = models.ForeignKey(ForumThread, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)  # Soft delete for posts

    def __str__(self):
        return f'Post by {self.created_by} in {self.thread}'

class ForumReply(models.Model):
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE, related_name='replies')
    content = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)  # Soft delete for replies

    def __str__(self):
        return f'Reply by {self.created_by} to Post ID {self.post.id}'
    