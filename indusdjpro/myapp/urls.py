from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('home',views.homepage,name='home'),
    path('about',views.aboutpage,name='about'),
    path('contact',views.contactpage,name='contact'),
]
