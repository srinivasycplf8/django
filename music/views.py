from django.shortcuts import render
from .models import Album

##to import html code

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


#for example if u have only 2 albums
#and u tyoed music/3
#which we didn't created yet....***so we request an HTTP****

from django.http import Http404

def index(request):
    all_albums=Album.objects.all()



    context={
        'all_albums':all_albums
    }
    

    return render(request,'music/index.html',context)

def detail(request,album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request,'music/detail.html',{'album':album})