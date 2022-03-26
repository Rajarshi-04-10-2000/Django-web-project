from django.contrib import admin
from django.urls import path
from home import views

#S-1 imported views

urlpatterns = [
    #if any request comes send it to index function of views and name this path as home
    path("", views.index, name='home'),  # note use comma kyu ki dict
    #now goto views.py of home and create index function
    #creating an about page
    path("about", views.about, name='about'),
    #now goto views.py of home and create about function
    #creating an services page
    path("services", views.services, name='services'),
    #now goto views.py of home and create services function
    path("contacts", views.contacts, name='contacts'),
    path("output", views.output, name='output'),







 ]
