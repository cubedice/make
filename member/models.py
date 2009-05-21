from django.db import models
from django.contrib.auth.models import User

class Member(User):
    signature = models.CharField(max_length=200)
