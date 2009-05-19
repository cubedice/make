from make.blog.models import Post
from django.shortcuts import render_to_response, get_object_or_404

def view_post(request, post_title):
	post = get_object_or_404(Post, pk = post_title)
	return render_to_response('post.html', {"post":post})
	
