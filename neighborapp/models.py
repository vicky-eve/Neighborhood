from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField


# Create your models here.
class Neighborhood(models.Model):
    name = models.TextField(max_length=100)
    location = models.CharField(max_length=100)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="hood",null=True)
    health_contact = PhoneField(null=True, blank=True)
    police_contact = PhoneField(null=True, blank=True)

