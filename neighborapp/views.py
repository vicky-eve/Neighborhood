from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from neighborapp.models import Neighborhood, Profile, Business, Post, User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, NeighborhoodSerializer, BusinessSerializer, PostSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from django.http import HttpResponse, HttpResponseRedirect, Http404
from.forms import RegistrationForm, UpdateProfileForm
from django.contrib import messages


#api views
class NeighborhoodtList(APIView):
    def get(self, request, format=None):
        all_neighborhoods = Neighborhood.objects.all()
        serializers = NeighborhoodSerializer(all_neighborhoods, many=True)
        return Response(serializers.data)
        

    def post(self, request, format=None):
        serializers = NeighborhoodSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)

class NeighborhoodDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_neighborhood(self, pk):
        try:
            return Neighborhood.objects.get(pk=pk)
        except Neighborhood.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        neigborhood = self.get_neighborhood(pk)
        serializers = NeighborhoodSerializer(neigborhood)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        neighborhood = self.get_neighborhood(pk)
        serializers = NeighborhoodSerializer(neighborhood, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        neighborhood = self.get_neighborhood(pk)
        neighborhood.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)

class ProfileDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_profile(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_profile(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BusinessList(APIView):
    def get(self, request, format=None):
        all_business = Business.objects.all()
        serializers = BusinessSerializer(all_business, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = BusinessSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)

    

class BusinessDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_business(self, pk):
        try:
            return Business.objects.get(pk=pk)
        except Business.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        business = self.get_business(pk)
        serializers = BusinessSerializer(business)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        business = self.get_business(pk)
        serializers = BusinessSerializer(business, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        business = self.get_business(pk)
        business.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PostList(APIView):
    def get(self, request, format=None):
        all_posts = Post.objects.all()
        serializers = PostSerializer(all_posts, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = PostSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)

    

class PostDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_post(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializers = PostSerializer(post)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        post = self.get_post(pk)
        serializers = PostSerializer(post, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_post(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#create views here
def index(request):
    return render (request, 'index.html')

@login_required(login_url='/accounts/login')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    return render(request, 'registration/profile.html', {"profile":profile})

def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user_id = user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
            form = UpdateProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():  
                profile = form.save(commit=False)
                profile.save()
                return redirect('profile') 
            
    return render(request, 'registration/update_profile.html', {"form":form, "profile":profile, 'id':id})

@login_required(login_url='/accounts/login/')
def create_business(request):
    business = Business.objects.all().order_by('-id')
    if request.method == 'POST':  
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            commit = form.save(commit=False)
            commit.user = request.user
            commit.save()
            return redirect('index')
    
    else:
        form = BusinessForm() 
    return render (request, 'create_biz.html', {'form':form, 'business':business})

@login_required(login_url="/accounts/login/")
def business(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    businesses = Business.objects.all().order_by('-id')

    if profile is None:
        profile = Profile.objects.filter(
            user_id=current_user.id).first()
        businesses = Business.objects.all().order_by('-id')
        neighborhood = Neighborhood.objects.all()
        
        
        
        return render(request, "registration/profile.html", {"danger": "Update Profile","neighborhood": neighborhood, "businesses": businesses})
    else:
        neighborhood = profile.neighborhood
        businesses = Business.objects.all().order_by('-id')
        return render(request, "business.html", {"businesses": businesses})