from music.views import AlbumDelete
from . import views
from django.urls import path,re_path

app_name='music'

urlpatterns = [
  
    re_path(r'^$', views.IndexView.as_view(),name="index"),

    ##whenever I click the album,it gives mae all songs
    #so we have to pass an id 

    #/music/712/

    re_path(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name="detail"),

    #music/album/add/

    re_path(r'album/add/$',views.AlbumCreate.as_view(),name="album-add"),

    #music/album/2/

    re_path(r'^album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(),name="album-update"),

    #music/album/2/delete

    re_path(r'album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(),name="album-delete"),




    
]