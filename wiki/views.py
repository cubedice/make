from make.wiki.models import Page, Edit
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import permission_required
from make.utils.http import render
import datetime
import markdown


def view_page(request, page_title):
    page = get_object_or_404(Page, pk = page_title)
    if request.method == 'POST':
        return save_page(request, page_title)
    content = page.content
    return render("wiki/view", dict({"page":page, "content":markdown.markdown(content)}))

@permission_required('wiki.change_page')
def edit_page(request, page_title):
    page = get_object_or_404(Page, pk = page_title)
    content = page.content
    return render("wiki/edit", dict({ "page":page }))

def save_page(request, page_title):
    content = request.POST["content"]
    try:
        page = Page.objects.get(pk = page_title)
        edit = Edit(editor = request.user, before = page.content, after = content, pub_date=datetime.datetime.now())
        edit.save()
        page.content = content
        page.edits.add(edit)
    except Page.DoesNotExist:
        page = Page( title = page_title, content = content)
    page.save()
    return HttpResponseRedirect("/wiki/"+page.slug+"/")

@permission_required('wiki.add_page')
def create_page(request):
    if request.method == 'POST':
        page = Page( title = request.POST['title'], content = request.POST['content'])
        page.save()
        return HttpResponseRedirect("/wiki/"+page.slug+"/")
    return render("wiki/new")
