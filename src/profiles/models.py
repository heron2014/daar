from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    bio = models.CharField(max_length=180, blank=True, null=True)
    picture = models.ImageField(upload_to='profile_images', blank=True, null=True)

    def __unicode__(self):
        return self.user.username


def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)
# Signal while saving user
post_save.connect(create_profile, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         profile, created = UserProfile.objects.get_or_create(user=instance)
# post_save.connect(create_profile, sender=User)
