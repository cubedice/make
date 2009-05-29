import datetime
from haystack import indexes
from haystack.sites import site
from make.blog.models import BlogPost

class BlogPostIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr = 'title')
    body = indexes.CharField(model_attr = 'body')
    author = indexes.CharField(model_attr = 'author')
    pub_date = indexes.DateTimeField(model_attr = 'pub_date')
    tags = indexes.CharField(model_attr = 'tags')

site.register(BlogPost, BlogPostIndex)
