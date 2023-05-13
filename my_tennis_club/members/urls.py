from django.urls import path
from . import views

urlpattenrs = [
     path('donkey/', views.hello,name ='members')
]