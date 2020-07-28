from django.shortcuts import render,get_object_or_404
from .models import Album,Song

##to import html code

from django.shortcuts import render

# Create your views here.


#for example if u have only 2 albums
#and u tyoed music/3
#which we didn't created yet....***so we request an HTTP****


def index(request):
    all_albums=Album.objects.all()



    context={
        'all_albums':all_albums
    }
    

    return render(request,'music/index.html',context)

def detail(request,album_id):
    album = get_object_or_404(Album,pk=album_id)
    return render(request,'music/detail.html',{'album':album})


def favorite(request,album_id):
    album = get_object_or_404(Album,pk=album_id)
    try:
        selected_song=album.song_set.get(pk=request.POST['song'])
    except (KeyError,Song.DoesNotExist):
        return render(request,'music/detail.html',{
            'album':album,
            'error_message':"You did not selext a valid song"
        
        })
    else:
        selected_song.is_favorite=True
        selected_song.save()
        return render(request,'music/detail.html',{'album':album})
