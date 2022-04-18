from django.contrib import admin
from .models import Neighborhood, Post, Business, Profile

# Register your models here.
admin.site.register(Neighborhood)
admin.site.register(Post)
admin.site.register(Business)
admin.site.register(Profile)