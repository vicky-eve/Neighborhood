from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from cloudinary.models import CloudinaryField

# Create your models here.
class Neighborhood(models.Model):
    name = models.TextField(max_length=100)
    location = models.CharField(max_length=100)
    photo = CloudinaryField('images', null=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="hood",null=True)
    occupants_count = models.IntegerField(default=0,blank=True, null=True)
    health_contact = PhoneField(null=True, blank=True)
    police_contact = PhoneField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null = True, related_name='user')
    
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
    biz_name = models.TextField(max_length=100, null=True)
    email_address = models.EmailField(max_length=100, null=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='neighborhood')
    contact = PhoneField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_biz')
    def __str__(self):
        return f'{self.biz_name} Business'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def update_business(self):
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
    profile_pic = CloudinaryField('images', null=True)
    gen_location = models.TextField(max_length=100)
    nei_name = models.TextField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def update_profile(self):
        self.update()

    def __str__(self):
        return f'{self.username} Profile'

class Post(models.Model):
    image = CloudinaryField('images', null=True)
    title = models.CharField(max_length=120, null=True)
    content = models.CharField(max_length=400,null=True)
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    neighbourhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='neighbourhood')

    def __str__(self):
        return f'{self.image} Post'
