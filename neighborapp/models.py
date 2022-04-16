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

    
    def __str__(self):
        return f'{self.name} hood'

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()
        
    def update_neighborhood(self):
        self.update()

    def update_occupants(self):
        self.update()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)

class Business(models.Model):
    biz_name = models.TextField(max_length=100)
    email_address = models.EmailField(max_length=100)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='neighborhood')

    def __str__(self):
        return f'{self.biz_name} Business'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def update_neighborhood(self):
        self.update()

    @classmethod
    def find_business(cls, business_id):
        return cls.objects.filter(id=business_id)

    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(name__icontains=name).all()

class Profile(models.Model):
    username =models.TextField(max_length=100)
    about = models.TextField(max_length=500)
    gen_location = models.TextField(max_length=100)
    nei_name = models.TextField(max_length=100)
    
