from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is the Music APP</h1>")

def detail(request,album_id):
    return HttpResponse("<h2>Details of the songs are"+str(album_id)+"</h2>")