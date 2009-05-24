from make.blog.models import BlogPost
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.http import HttpRequest, HttpResponseRedirect

def view_post(request, post_title):
    post = get_object_or_404(BlogPost, pk = post_title)
    return render_to_response('blog/post.html', {"post":post})

@permission_required('blog.add_post')
def create_post(request):
    return render_to_response('blog/create.html')

def save_post(request):
    post_title = request.POST["title"]
    content = request.POST["content"]
    post = BlogPost( title = post_title, body = content, author = request.user)
    post.save()
    return HttpResponseRedirect("/blog/"+post_title+"/")

@permission_required('blog.add_post')
def edit_post(request, post_title):
    post = get_object_or_404(BlogPost, pk=post_title)
    return render_to_response('blog/edit.html', {"post":post})
