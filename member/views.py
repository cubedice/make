#from make.member.models import Member
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponseRedirect
from make.member.models import UserProfile, NewUserForm, EditProfileForm

def self_profile(request):
    username = request.user.username
    return profile(request, username)

def profile(request, username):
    member = get_object_or_404(User, username=username)
    profile = member.get_profile()
    if request.user.is_authenticated(): 
        return edit_profile(request, member, profile)
    return render_to_response('member/profile.html',{'member':member, 'profile':profile})    

@login_required
def edit_profile(request, member, profile):
    if not member==request.user:
        return render_to_response('member/profile.html',{'member':member, 'profile':profile})   

    if request.method == 'POST':
        form = EditProfileForm(request.POST)
        # TODO: userprof.save()
        if form.is_valid():
            member.email = form.cleaned_data['email']
            member.first_name = form.cleaned_data['first_name']
            member.last_name = form.cleaned_data['last_name']
            profile.url = form.cleaned_data['url']
            profile.signature = form.cleaned_data['signature']
            member.save()
            profile.save()
        return HttpResponseRedirect('/profile/'+member.username+'/')

    form = EditProfileForm({'email':member.email, 'first_name':member.first_name, 'last_name':member.last_name, 'url':profile.url, 'signature':profile.signature}, instance=profile)
    if form.is_valid():
        form.save()
    return render_to_response('member/edit_profile.html',{'member':member, 'form':form})    


def create_profile(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            # TODO: create_user()
            return HttpResponseRedirect('member/thanks.html')
    else:
        form = NewUserForm()
    return render_to_response('member/create_profile.html', {"form":form})

