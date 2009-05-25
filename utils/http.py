from django.shortcuts import render_to_response  
from django.template import RequestContext  
from django.http import HttpResponse, HttpResponseRedirect  
from make.middleware import threadlocals as tl  

def render(template_name, dictionary=None):      
    dictionary = dictionary or dict()  
    return render_to_response(template_name + ".html", dictionary,  
        context_instance=RequestContext(tl.get_request()))  

