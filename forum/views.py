from make.forum.models import Category, Thread, ForumPost
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from make.utils.http import render

def index(request):
    category_list = Category.objects.all() 
    return render('forum/index',dict({'category_list':category_list}))

def category(request, category_title):
    category = get_object_or_404(Category,slug = category_title)
    if request.method == 'POST':
        thread = Thread ( poster = request.user, topic = request.POST['title'], description = request.POST['body'], category = category )
        thread.save()
    return render('forum/category', dict({"category":category, "thread_list":category.thread_set.all()}))

def thread(request, category_title, thread_title):
    thread = get_object_or_404(Thread, slug=thread_title)
    if request.method == 'POST':
        post = ForumPost( poster=request.user, thread=thread, body=request.POST['body'], isSticky=False)
        post.save()
    return render('forum/thread', dict({"thread":thread, "post_list":thread.forumpost_set.all()}))
