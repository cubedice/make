from make.forum.models import Category
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    category_list = Category.objects.all() 
    return render_to_response('forum/index.html',{'category_list':category_list})

def category(request, category_title):
    category = get_object_or_404(Category,pk = category_title)
    return render_to_response('forum/'+category_title+'/', {"thread_list":category.thread_set})
