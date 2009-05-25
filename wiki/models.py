from django.db import models
from django.contrib.auth.models import User
from make.utils.models import AutoSlug

class Edit(models.Model):
    editor = models.ForeignKey(User)
    before = models.TextField(blank=True)
    after = models.TextField(blank=True)
    pub_date = models.DateTimeField('date edited')
    def __unicode__(self):
        return "by " + self.editor.username + " on " + str(self.pub_date) 
    

class Page(models.Model):
    title = models.CharField(max_length = "80")
    slug = models.SlugField(unique=True, primary_key = True)  
    content = models.TextField(blank=True)
    edits = models.ManyToManyField(Edit, blank=True)
    def save(self):
        AutoSlug.unique_slug(self, slug_source='title', slug_field='slug')
        super(Page, self).save()
    def __unicode__(self):
        return self.title
