from django.contrib import admin
from django.urls import path
from Hello import views

urlpatterns = [
   path('', views.index, name='home'),
   path("about", views.about, name='about'),
   path("home", views.index, name='home'),
   path("contact", views.contact, name='contact'),
   path("result", views.result, name='result'),
   path("postq", views.postq, name='result'),
]