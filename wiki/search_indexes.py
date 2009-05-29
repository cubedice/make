import datetime
from haystack import indexes
from haystack.sites import site
from make.wiki.models import Page

class PageIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr = 'title')
    content = indexes.CharField(model_attr = 'content')    


site.register(Page, PageIndex)
