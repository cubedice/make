from django.db import models
from django.contrib.auth.models import User
from django import forms


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, primary_key=True)
    url = models.URLField(blank=True)
    signature = models.CharField(max_length="140")

class NewUserForm(forms.ModelForm):
    password = forms.CharField(max_length="140", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','password','email'] 

class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length="140", required=False)
    last_name = forms.CharField(max_length="140", required=False)
    email = forms.EmailField(required=False)
    class Meta:
        model = UserProfile
        exclude = ('user',)
