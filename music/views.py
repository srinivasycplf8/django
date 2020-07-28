from django.shortcuts import render
from .models import Album

##to import html code

from django.template import loader

# Create your views here.
from django.http import HttpResponse

def index(request):
    all_albums=Album.objects.all()


    template=loader.get_template('music/index.html')

    context={
        'all_albums':all_albums
    }
    

    return HttpResponse(template.render(context,request))

def detail(request,album_id):
    return HttpResponse("<h2>Details of the songs are"+str(album_id)+"</h2>")