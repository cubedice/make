from make.projects.models import Project, ProjectForm
from make.forum.models import Thread, Category
from make.wiki.models import Page
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.http import HttpRequest, HttpResponseRedirect
from make.utils.http import render

def index(request):
    latest_projects = Project.objects.all().order_by('-last_update')[:5]
    return render('projects/index', dict(latest_projects=latest_projects))

def view_project(request, project_title):
    project = get_object_or_404( Project, pk = project_title )
    return render('projects/view_project', dict(project=project))

def edit_project(request, project_title):
    project = get_object_or_404( Project, pk = project_title )
    if request.method == 'POST':
        return save_project(request, project_title)
    form =  ProjectForm( instance = instance )
    return render('projects/edit_project', dict( form=form ))

def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            import datetime
            category = get_object_or_404( Category, pk = 'Projects' )
            forum_thread = Thread( topic = form.cleaned_data['title'], poster = request.user, category = category, description = "Login to discuss this project.")
            forum_thread.save()
            wiki_page = Page( title = form.cleaned_data['title'] )
            wiki_page.save()
            newproj = Project( title = form.cleaned_data['title'], owner = form.cleaned_data['owner'], last_update = datetime.datetime.now(), status = form.cleaned_data['status'], description = form.cleaned_data['description'],documentation = form.cleaned_data['documentation'],wiki_page = wiki_page,forum_thread = forum_thread)       
            newproj.save()
            return HttpResponseRedirect("/projects/"+newproj.slug+"/")
    form = ProjectForm()
    return render('projects/create', dict(form = form))

def save_project(request, project_title):
    import datetime
    project = get_object_or_404( pk = page_title )
    project.last_update = datetime.datetime.now()
    form = ProjectForm(request.POST, instance = project)
    if form.is_valid():
        form.save()
    project.save()
    return HttpResponseRedirect("/project/"+projects.slug+"/")
