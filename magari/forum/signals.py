from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ForumReply
from .models import Notification  # Assuming you have a Notification model

@receiver(post_save, sender=ForumReply)
def notify_on_reply(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            recipient=instance.post.created_by,
            actor=instance.created_by,
            verb="replied to your post",
            target=instance.post,
        )