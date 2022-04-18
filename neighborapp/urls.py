from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('profile/', views.profile, name='profile'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/profile/', views.profile, name='profile'),
    path('hood/', views.hood, name='hood'),
    path('one_hood/', views.one_hood, name='one_hood'),
    path('search/', views.search, name='search_biz'),
    path('create_post/', views.create_post, name='create_post'),
    path('accounts/profile/', views.profile, name='profile'),
    path('create_neighborhood/', views.create_neighborhood, name='create_neighborhood'),
    path('create_business/', views.create_business, name='create_business'),
    path('api/post/', views.PostList.as_view()),
    path('api/profile/', views.ProfileList.as_view()),
    path('api/business/', views.BusinessList.as_view()),
    path('api/neighborhood/', views.NeighborhoodList.as_view()),
    path('api/merch/post-id/(?P<pk>[0-9]+)/',views.PostDescription.as_view()),
    path('api/merch/profile-id/(?P<pk>[0-9]+)/',views.ProfileDescription.as_view()),
    path('api/merch/business-id/(?P<pk>[0-9]+)/',views.BusinessDescription.as_view()),
    path('api/merch/neighborhood-id/(?P<pk>[0-9]+)/',views.NeighborhoodDescription.as_view()),
]