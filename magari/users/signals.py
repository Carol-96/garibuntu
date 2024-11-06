from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    # Use get_or_create to avoid duplicate creation attempts
    if created:
        Profile.objects.get_or_create(user=instance)
    else:
        # For existing users, save the profile if it exists
        if hasattr(instance, 'profile'):
            instance.profile.save()
