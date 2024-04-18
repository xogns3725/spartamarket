from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    following = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers"
    )
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)