from django.db import models
from django.contrib.auth.models import User
from make.utils.models import AutoSlug

class Category(models.Model):
    name = models.CharField(blank=False, max_length=100, primary_key=True)
    slug = models.SlugField(unique=True)
    def __unicode__(self):
        return self.name
    def save(self):
        AutoSlug.unique_slug(self, slug_source='name', slug_field='slug')
        super(Category, self).save()

class Thread(models.Model):
    topic = models.CharField(blank=False, max_length=90, primary_key=True)
    slug = models.SlugField(unique=True)
    poster = models.ForeignKey(User)
    description = models.CharField(blank=True, max_length=400)
    category = models.ForeignKey(Category)
    def __unicode__(self):
        return self.topic
    def save(self):
        AutoSlug.unique_slug(self, slug_source='topic', slug_field='slug')
        super(Thread, self).save()

class Poll(Thread):
    yeas = models.PositiveIntegerField()
    nays = models.PositiveIntegerField()

class ForumPost(models.Model):
    isSticky = models.BooleanField()
    poster = models.ForeignKey(User)
    thread = models.ForeignKey(Thread)
    body = models.TextField(blank = False) 

