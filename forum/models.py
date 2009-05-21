from django.db import models
from django.contrib.auth.models import User

class Thread(models.Model):
    topic = models.CharField(blank=False, max_length=90)

class Poll(Thread):
    yeas = models.PositiveIntegerField()
    nays = models.PositiveIntegerField()
    description = models.TextField(blank = False) 

class ForumPost(models.Model):
    isSticky = models.BooleanField()
    poster = models.ForeignKey(User)
    thread = models.ForeignKey(Thread)
    body = models.TextField(blank = False) 

