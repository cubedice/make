from make.projects.models import Project
from make.forum.models import Thread, Category
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.http import HttpRequest, HttpResponseRedirect
from make.utils.http import render

def index(request):
    latest_projects = Project.objects.all().order_by('-last_update')[:5]
    return render('projects/index', dict(latest_projects=latest_projects))
    

# todo: add permission deco
def save_project(request):
    title = request.POST["title"]
    content = request.POST["content"]
    import datetime
    category = get_object_or_404( Category, pk = 'Blog' )
    forumthread = Thread( topic = title, poster = request.user, category = category, description = "Login to discuss this blag post.")
    forumthread.save()
    project = Project( title = post_title, body = content, author = request.user, pub_date=datetime.datetime.now(), forumthread = forumthread )
    project.save()
    return HttpResponseRedirect("/project/"+project.slug+"/")
