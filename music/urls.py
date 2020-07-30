from . import views
from django.urls import path,re_path

app_name='music'

urlpatterns = [
    #the '' is used when the user didin't select specific song or default it
    #goes to views page and their function mae called index 
    #so whathtver it does it returns our value

    ##for using regular expression we have to use re_path
    ##instead of ""path"""
    re_path(r'^$', views.IndexView.as_view(),name="index"),

    ##whenever I click the album,it gives mae all songs
    #so we have to pass an id 

    #/music/712/

    re_path(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name="detail"),

    #music/album/add/

    re_path(r'album/add/$',views.AlbumCreate.as_view(),name="album-add"),




    
]