from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Album,Song
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import JsonResponse



class IndexView(generic.ListView):
    template_name='music/index.html'
    context_object_name='all_albums'
    
    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model=Album
    template_name='music/detail.html'

class SongView(generic.ListView):
    template_name='music/songs.html'
    context_object_name='song_list'
    def get_queryset(self):
        return Song.objects.all()

  
class AlbumCreate(CreateView):
    model=Album
    fields=['artist','album_title','genre','album_logo']

class SongCreate(CreateView):
    model=Song
    fields=['song_title','file_type']
   

    def form_valid(self, form):
        album = get_object_or_404(Album, pk=self.kwargs['pk'])
        form.instance.album = album
        return super(SongCreate, self).form_valid(form)

class AlbumUpdate(UpdateView):
    model=Album
    fields=['artist','album_title','genre','album_logo']


class AlbumDelete(DeleteView):
    model=Album
    success_url=reverse_lazy('music:index')

def delete_song(request, album_id, song_id):
    album = get_object_or_404(Album, pk=album_id)
    song = Song.objects.get(pk=song_id)
    song.delete()
    return render(request, 'music/detail.html', {'album': album})

def favorite(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    try:
        if song.is_favorite:
            song.is_favorite = False
        else:
            song.is_favorite = True
        song.save()
    except (KeyError, Song.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})
   

#class AddSong(CreateView):
 #   model=Song
  #  fields=['song_title','file_type']

class UserFormView(View):

    form_class=UserForm
    template_name="music/registration_form.html"
    
    #display blank form
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    #processs form data
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user=form.save(commit=False)


            username=form.cleaned_data['username']
            password=form.cleaned_data['password']


            user.set_password(password)
            user.save()


            #returns User Objects if credentials are correct

            user=authenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    #then you logged in
                    login(request,user)
                    return redirect('music:index')

        #try again 

        return render(request,self.template_name,{'form':form})
            


        


