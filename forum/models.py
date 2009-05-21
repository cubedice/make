from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(blank=False, max_length=100, primary_key=True)
    slug = models.SlugField(unique=True)  
    def __unicode__(self):
        return self.name


class Thread(models.Model):
    topic = models.CharField(blank=False, max_length=90)
    slug = models.SlugField(unique=True)  
    category = models.ForeignKey(Category)
    def __unicode__(self):
        return self.topic


class Poll(Thread):
    yeas = models.PositiveIntegerField()
    nays = models.PositiveIntegerField()
    description = models.TextField(blank = False) 

class ForumPost(models.Model):
    isSticky = models.BooleanField()
    poster = models.ForeignKey(User)
    thread = models.ForeignKey(Thread)
    body = models.TextField(blank = False) 

