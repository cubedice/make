from make.forum.models import Post, Thread
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    thread_list = Thread.objects.all() 
    render_to_response('forum/index.html',{'thread_list':thread_list})
