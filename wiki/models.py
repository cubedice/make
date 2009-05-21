from django.db import models
from django.contrib.auth.models import User

class Edit(models.Model):
    editor = models.ForeignKey(User)
    before = models.TextField(blank=True)
    after = models.TextField(blank=True)

class Page(models.Model):
    title = models.CharField(max_length = "80", primary_key = True)
    slug = models.SlugField(unique=True)  
    content = models.TextField(blank=True)
    edits = models.ManyToManyField(Edit)
