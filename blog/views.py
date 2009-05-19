from make.blog.models import Post
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required

def view_post(request, post_title):
	post = get_object_or_404(Post, pk = post_title)
	return render_to_response('post.html', {"post":post})

@login_required
def create_post(request, post_title):
	content = ""
    return render_to_response('blog/create.html', {"post_title":post_title, "content":content}

