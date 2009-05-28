from django.db import models
from make.member.models import User
from make.forum.models import Thread
from make.wiki.models import Page

class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, primary_key=True)  
    owner = models.ForeignKey(User)
    last_update = models.DateTimeField('date last updated')
    status = models.CharField(max_length=100)
    description = models.TextField()
    documentation = models.TextField()
    wiki_page = models.ForeignKey(Page)
    forum_thread = models.ForeignKey(Thread)
    def save(self):
        AutoSlug.unique_slug(self, slug_source='title', slug_field='slug')
        super(Project, self).save()
    def __unicode__(self):
        return self.title
