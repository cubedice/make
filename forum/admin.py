from make.forum.models import ForumPost, Thread, Poll, Category
from django.contrib import admin

admin.site.register(ForumPost)
admin.site.register(Thread)
admin.site.register(Poll)
admin.site.register(Category)
