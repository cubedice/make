import datetime
from haystack import indexes
from haystack.sites import site
from make.forum.models import ForumPost, Thread, Poll

class ForumPostIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    thread = indexes.CharField(model_attr = 'thread')
    body = indexes.CharField(model_attr = 'body')
    poster = indexes.CharField(model_attr = 'poster')

class PollIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    topic = indexes.CharField(model_attr = 'topic')
    poster = indexes.CharField(model_attr = 'poster')
    description = indexes.CharField(model_attr = 'description')


class ThreadIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    topic = indexes.CharField(model_attr = 'topic')
    poster = indexes.CharField(model_attr = 'poster')
    description = indexes.CharField(model_attr = 'description')
    


site.register(ForumPost, ForumPostIndex)
site.register(Thread, ThreadIndex)
site.register(Poll, PollIndex)
