from django.db import models
from django.contrib.auth.models import User
from make.utils.models import AutoSlug

class Edit(models.Model):
    editor = models.ForeignKey(User)
    before = models.TextField(blank=True)
    after = models.TextField(blank=True)

class Page(models.Model):
    title = models.CharField(max_length = "80", primary_key = True)
    slug = models.SlugField(unique=True)  
    content = models.TextField(blank=True)
    edits = models.ManyToManyField(Edit)
    def save(self):
        AutoSlug.unique_slug(self, slug_source='title', slug_field='slug')
        super(Page, self).save()
