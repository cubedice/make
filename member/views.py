#from make.member.models import Member
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from make.member.models import UserProfile, NewUserForm, EditProfileForm
from make.utils.http import render

def self_profile(request):
    username = request.user.username
    return HttpResponseRedirect('/profile/'+username+'/')

def profile(request, username):
    member = get_object_or_404(User, username=username)
    profile = member.get_profile()
    if request.user.is_authenticated(): 
        return edit_profile(request, member, profile)
    return render('member/profile',dict({'profile':profile, 'member':member}))    

@login_required
def edit_profile(request, member, profile):
    if not member==request.user:
        return render('member/profile',dict({'profile':profile}))   
    if request.method == 'POST':
        form = EditProfileForm(request.POST)
        if form.is_valid():
            member.email = form.cleaned_data['email']
            member.first_name = form.cleaned_data['first_name']
            member.last_name = form.cleaned_data['last_name']
            profile.url = form.cleaned_data['url']
            profile.signature = form.cleaned_data['signature']
            member.save()
            profile.save()
        return render('member/edit_profile', dict({'form':form}))

    form = EditProfileForm({'email':member.email, 'first_name':member.first_name, 'last_name':member.last_name, 'url':profile.url, 'signature':profile.signature}, instance=profile)
    if form.is_valid():
        form.save()
    return render('member/edit_profile',dict({'form':form}))    


def create_profile(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            # create user and profile
            new_user = User.objects.create_user(username = form.cleaned_data['username'], email= form.cleaned_data['email'], password = form.cleaned_data['password'])
            new_user.is_staff = False
            new_user.is_active = True
            new_profile = UserProfile.objects.create(user=new_user)
            new_profile.save()
            new_user.save()
            # log the user in
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            login(request, user)
            return profile(request, new_user.username)
    else:
        form = NewUserForm()
    return render('member/create_profile', dict({"form":form}))

