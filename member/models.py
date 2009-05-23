from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    url = models.URLField()
    phone_number = models.CharField(max_length="8")
    signature = models.CharField(max_length="140")
    user = models.ForeignKey(User, unique=True, primary_key=True)
