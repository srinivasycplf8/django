from django.contrib import admin
from .models import Album,Song

# Register your models here.

admin.site.register(Album)
#No need to migrate the reason is we 
#are adding songs to the album
#we are not creating a new table here
admin.site.register(Song)