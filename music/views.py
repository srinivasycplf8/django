from django.shortcuts import render
from .models import Album

# Create your views here.
from django.http import HttpResponse

def index(request):
    html=''
    albums=Album.objects.all()
    for album in albums:
        url="/music/"+str(album.id)+"/"
        html+='<a href=" '+ url +'">' + album.album_title + '</a><br>'


    return HttpResponse(html)

def detail(request,album_id):
    return HttpResponse("<h2>Details of the songs are"+str(album_id)+"</h2>")