from django.db import models
from django.contrib.auth.models import User
from make.utils.models import AutoSlug
from django import forms

class Tag(models.Model):
    name = models.CharField(max_length = "80", primary_key = True)

class BlogPost(models.Model):
    title = models.CharField(max_length = "80", unique=False)
    slug = models.SlugField(unique=True, primary_key=True)  
    pub_date = models.DateTimeField('date published')
    body = models.TextField(blank = False) 
    author = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag, blank=True)
    def save(self):
        AutoSlug.unique_slug(self, slug_source='title', slug_field='slug')
        super(BlogPost, self).save()
    def __unicode__(self):
        return self.title


