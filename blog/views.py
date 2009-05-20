from make.blog.models import Post
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import permission_required

def view_post(request, post_title):
    post = get_object_or_404(Post, pk = post_title)
    return render_to_response('blog/post.html', {"post":post})

@permission_required('blog.add_post')
def create_post(request):
    content = ""
    return render_to_response('blog/create.html')
