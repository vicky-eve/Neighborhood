from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.
class NeighborhoodTestClass(TestCase):
    def setUp(self):
        self.neighborhood = Neighborhood(title='Test Neighborhood')

    def test_instance(self):
        self.assertTrue(isinstance(self.neighborhood, Neighborhood))

    def test_save_method(self):
        self.neighborhood.save()
        neighborhoods = Neighborhood.objects.all()
        self.assertTrue(len(neighborhoods) > 0)

    def test_delete_method(self):
        self.neighborhood.save()
        self.neighborhood.delete_neighborhood()
        neighborhoods = Neighborhood.objects.all()
        self.assertTrue(len(neighborhoods) == 0)

class BusinessTestClass(TestCase):
    def setUp(self):
        self.business = Business(name='Test Business')

    def test_instance(self):
        self.assertTrue(isinstance(self.business, Business))

    def test_save_method(self):
        self.business.save()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) > 0)

    def test_delete_method(self):
        self.business.save()
        self.business.delete_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) == 0)
