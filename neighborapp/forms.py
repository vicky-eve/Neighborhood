from .models import Business, Neighborhood, Post, Profile
from django.forms import ModelForm
from django import forms


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username','about','profile_pic', 'gen_location','nei_name') 

class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        fields=['biz_name','email_address','contact']

class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ('admin',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['title','content','image']