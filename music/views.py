from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Album
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm

class IndexView(generic.ListView):
    template_name='music/index.html'
    context_object_name='all_albums'
    
    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model=Album
    template_name='music/detail.html'

  
class AlbumCreate(CreateView):
    model=Album
    fields=['artist','album_title','genre','album_logo']

class AlbumUpdate(UpdateView):
    model=Album
    fields=['artist','album_title','genre','album_logo']


class AlbumDelete(DeleteView):
    model=Album
    success_url=reverse_lazy('music:index')

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
            #here we are storing information 
            #and we are doing further validation
            user=form.save(commit=False)
            #at this point it won't save database but it stores locally

            #cleaned normalized data
            #like for example everoune using a date format

            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            #the cleaned_data acts like a dictorinay so the keys ar einside and it gives
            #the value

            #Now if you want to change the password

            user.set_password(password)
            user.save()
            
            

        


