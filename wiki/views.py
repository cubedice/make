from make.wiki.models import Page
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import permission_required
import markdown


def view_page(request, page_title):
    try:
        page = Page.objects.get(pk = page_title)
    except Page.DoesNotExist:
        return render_to_response("create.html", {"page_title":page_title})
    content = page.content
    return render_to_response("/blog/view.html", {"page_title":page_title, "content":markdown.markdown(content)})

@permission_required('wiki.change_page')
def edit_page(request, page_title):
    try:
        page = Page.objects.get(pk = page_title)
        content = page.content
    except Page.DoesNotExist:
        return create_page(request, page_title) 
    return render_to_response("/wiki/edit.html", {"page_title":page_title, "content":content})

def save_page(request, page_title):
    content = request.POST["content"]
    try:
        page = Page.objects.get(pk = page_title)
        page.content = content
    except Page.DoesNotExist:
        page = Page( title = page_title, content = content)
    page.save()
    return HttpResponseRedirect("/wiki/"+page_title+"/")

@permission_required('wiki.add_page')
def create_page(request, page_title):
    content = ""
    return render_to_response("/wiki/edit.html", {"page_title":page_title, "content":content})
