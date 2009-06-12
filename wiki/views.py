from make.wiki.models import Page, Edit
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import permission_required
from make.utils.http import render
import datetime
import markdown

def index(request):
    freshest_pages = Page.objects.all().order_by('-last_edit')[:5]
    return render("wiki/index", dict(freshest_pages=freshest_pages))

def view_page(request, page_title):
    page = get_object_or_404(Page, pk = page_title)
    if request.method == 'POST':
        return save_page(request, page_title)
    content = page.content
    return render("wiki/view", dict({"page":page, "content":markdown.markdown(content)}))

def page_history(request, page_title):
    page = get_object_or_404(Page, pk = page_title)
    edits = page.edits.order_by('-pub_date')
    return render("wiki/history", dict({"page":page, "edits":edits}))


@permission_required('wiki.change_page')
def edit_page(request, page_title):
    page = get_object_or_404(Page, pk = page_title)
    content = page.content
    return render("wiki/edit", dict({ "page":page }))

def save_page(request, page_title):
    content = request.POST["content"]
    try:
        page = Page.objects.get(pk = page_title)
        from difflib import context_diff
        import re
        diff = context_diff(page.content.splitlines(), content.splitlines(), 3)
        before_start = re.compile(r'[*]{3}\s(?P<start>[0-9]+)[,](?P<end>[0-9]+)\s[*]{3}')
        after_start = p = re.compile(r'[-]{3}\s(?P<start>[0-9]+)[,](?P<end>[0-9]+)\s[-]{3}')
        before = ''
        after = ''
        for line in diff:
            if(before_start.search(line)):
                before += line + '\n'
                while True:
                    try:
                        line = diff.next()
                    except StopIteration:
                        break
                    if (after_start.search(line)):
                        break
                    if( line.startswith('!') ):
                        line = '<span class="reddiff">' + line + '</span>'
                    before += line + '\n'
            if( after_start.search(line) ):
                after += line + '\n'
                while True:
                    try:
                        line = diff.next()
                    except StopIteration:
                        break
                    if( before_start.search(line) ):
                        break
                    if( line.startswith('!') or line.startswith('+') ):
                        line = '<span class="greendiff">' + line + '</span>'
                    after += line  + '\n'

        edit = Edit(editor = request.user, before = before, after = after, pub_date=datetime.datetime.now())
        edit.save()
        page.content = content
        page.edits.add(edit)
    except Page.DoesNotExist:
        page = Page( title = page_title, content = content, last_edit=datetime.datetime.now())
    page.save()
    return HttpResponseRedirect("/wiki/"+page.slug+"/")

@permission_required('wiki.add_page')
def create_page(request):
    if request.method == 'POST':
        page = Page( title = request.POST['title'], content = request.POST['content'], last_edit=datetime.datetime.now())
        page.save()
        return HttpResponseRedirect("/wiki/"+page.slug+"/")
    return render("wiki/new")
