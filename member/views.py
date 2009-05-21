#from make.member.models import Member
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User

def profile(request, username):
    member = get_object_or_404(User, username=username)
    return render_to_response('member/profile.html',{'member':member})    
