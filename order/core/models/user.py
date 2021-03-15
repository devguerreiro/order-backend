from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True)

    # login by email
    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username"]