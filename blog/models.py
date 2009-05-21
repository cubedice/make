from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length = "80", primary_key = True)

class BlogPost(models.Model):
    title = models.CharField(max_length = "80", primary_key = True)
    slug = models.SlugField(unique=True)  
    body = models.TextField(blank = False) 
    author = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag, blank=True)

