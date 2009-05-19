from make.wiki.models import Page
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import markdown

def view_page(request, page_title):
	try:
		page = Page.objects.get(pk = page_title)
	except Page.DoesNotExist:
		return render_to_response("create.html", {"page_title":page_title})
	content = page.content
	return render_to_response("view.html", {"page_title":page_title, "content":markdown.markdown(content)})

@login_required
def edit_page(request, page_title):
	try:
		page = Page.objects.get(pk = page_title)
		content = page.content
	except Page.DoesNotExist:
		content = ""
	return render_to_response("edit.html", {"page_title":page_title, "content":content})

def save_page(request, page_title):
	content = request.POST["content"]
	try:
		page = Page.objects.get(pk = page_title)
		page.content = content
	except Page.DoesNotExist:
		page = Page( title = page_title, content = content)
	page.save()
	return HttpResponseRedirect("/wiki/"+page_title+"/")
