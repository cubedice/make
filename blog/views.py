from make.blog.models import BlogPost
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.http import HttpRequest, HttpResponseRedirect
from make.utils.http import render

def view_post(request, post_title):
    post = get_object_or_404(BlogPost, pk = post_title)
    return render('blog/post', dict({"post":post}))

@permission_required('blog.add_post')
def create_post(request):
    return render('blog/create')

def save_post(request):
    post_title = request.POST["title"]
    content = request.POST["content"]
    import datetime
    post = BlogPost( title = post_title, body = content, author = request.user, pub_date=datetime.datetime.now())
    post.save()
    return HttpResponseRedirect("/blog/"+post.slug+"/")

@permission_required('blog.add_post')
def edit_post(request, post_title):
    post = get_object_or_404(BlogPost, pk=post_title)
    if not post.author == request.user:
        return HttpResponseRedirect("/blog/"+post_title+"/")
    if request.method == 'POST':
        post.body = request.POST["content"]
        post.save()
        return HttpResponseRedirect("/blog/"+post.slug+"/")
    return render('blog/edit', dict({"post":post}))

def index(request):
    latest_posts = BlogPost.objects.all().order_by('-pub_date')[:5]
    return render('blog/index', dict(latest_posts=latest_posts))
