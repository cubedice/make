from haystack import indexes
from haystack.sites import site
from make.projects.models import Project

class ProjectIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr = 'title')
    description = indexes.CharField(model_attr = 'description')
    owner = indexes.CharField(model_attr = 'owner')

site.register(Project, ProjectIndex)
