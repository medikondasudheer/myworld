from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('hello/', views.hello, name='members'),
    path('hello/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'), 
]
