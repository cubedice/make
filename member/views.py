#from make.member.models import Member
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponseRedirect
from make.member.models import UserProfile

def profile(request, username):
    member = get_object_or_404(User, username=username)
    profile = get_object_or_404(UserProfile, pk=member)
    return render_to_response('member/profile.html',{'member':member, 'profile':profile})    

@login_required
def edit_profile(request, username):
    member = get_object_or_404(User, username=username)
    
    if not member==request.user:
        return render_to_response('member/profile.html',{'member':member, 'profile':profile})    

    return render_to_response('member/edit_profile.html',{'member':member, 'profile':profile})    


def create_profile(request):
    return render_to_response('member/create_profile.html')

def save_profile(request, username):
    signature = request.POST["signature"]
    member = get_object_or_404(User, username=username)
    profile = get_object_or_404(UserProfile, pk=member)
    profile.signature = signature
    profile.save()
    return HttpResponseRedirect("/accounts/"+username+"/")
