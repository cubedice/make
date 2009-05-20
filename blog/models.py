from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length = "80", primary_key = True)

class Post(models.Model):
    title = models.CharField(max_length = "80", primary_key = True)
    body = models.TextField(blank = False) 
    author = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag)

