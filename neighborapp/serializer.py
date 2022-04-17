from rest_framework import serializers
from .models import Profile, Neighborhood,  Business, Post

class NeighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = ('id', 'name', 'location', 'admin', 'health_contact', 'police_contact')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'username', 'about', 'gen_location', 'nei_name')

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ('id', 'biz_name', 'email_address')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'image', 'title', )