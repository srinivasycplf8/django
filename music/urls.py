from . import views
from django.urls import path

urlpatterns = [
    #the '' is used when the user didin't select specific song or default it
    #goes to views page and their function mae called index 
    #so whathtver it does it returns our value
    path('', views.index,name="index")
    dsxk
]