from django.db import models
from django.urls import reverse

# Create your models here.
#After creating a model...use cmd to activate these models

#In a music app we'' have artist name and album title.....so on
#and whaterver name we are specifying here shoudld be use again in a 
#datatabase

#AFter that python manage.py migrate
#first command makes the change firles and second one it runs it

#now our datyabase synced

class Album(models.Model):
     #the right value see which type of input it will accept
     #so the artist we''ll take as a string so it's a charfield

    artist=models.CharField(max_length=250)

    album_title=models.CharField(max_length=500)

    genre=models.CharField(max_length=100)

    album_logo=models.FileField()

    def get_absolute_url(self):
       return reverse('music:detail',kwargs={'pk':self.pk})


 
    def __str__(self):
        return self.album_title + '-' +self.artist

class Song(models.Model):
     
     #So each """ALBUM" has 12 to 15 songs

     #We gonna create as many albums we want 

     #but when we create a songs it should be associated to album

     #how to link this songs to a particular album????


     album=models.ForeignKey(Album,on_delete=models.CASCADE)

     file_type=models.FileField(default='')

     song_title=models.CharField(max_length=250)

     is_favorite=models.BooleanField(default=False)
     def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.album.id})
     def __str__(self):
        return self.song_title

     #****ABOUT IDS *****

     #Whenever we create this database for exampple we created the class "Album"
     #in that we created 4 variables it we created 4 columns in our database
     #And behind the scene Django makes an "**another coloumn****
     #for us that is primary key which is a unique identifer number and
     #that is also called primary key

     #So when we create the first album it gives an id number 1
     #whenever we create second album it increment by 1 which is 2 
     #and so on


     #Forieng key :: Each song is linked to an album
     #let's say album red has primary key 1
     #whenever we created a song we need to link it to album
     #the foreign key is gonna be one
     #we say whatever song is linked to primary key 1


     #delete cascade ::: let's say if u want to delete album
     #then no songs should be there ,,,so whenever delete album
     #the songs also will be removed



