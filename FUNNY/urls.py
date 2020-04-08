from django.contrib import admin
from django.urls import path
from . import views
#app_name="resume"
urlpatterns = [
    path('', views.getUserDetails, name='Upload Page'),
    path('UserDetails', views.UserDetails, name='UserDetails'),
    path('saveUserDetails', views.saveUserDetails, name='saveUserDetails'),

]