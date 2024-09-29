from django.shortcuts import render, redirect
from .models import Song
from .forms import SongForm

# Create your views here.
def index(request):
    songs = Song.objects.all()
    context = {
        'songs' : songs
    }
    
    return render(request, 'songs/index.html', context)

def create(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save()
            return redirect('songs:detail', song.pk)
    # new
    else:
        form = SongForm()
    context = {
        'form' : form
    }
    return render(request, 'create.html', context)
        
def detail(request, pk):
    song = Song.objects.get(pk=pk)
    context = {
        'song' : song
    }
    return render(request, 'songs/detail.html', context)
    
    
def update(request, pk):
    song = Song.objects.get(pk=pk)
    if request.method =='POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('songs:detail', song.pk)
    
    else:
        form = SongForm()
    context = {
        'song' : song,
        'form' : form
    }
    return render(request, 'songs/update.html', context)

def delete(request, pk):
    song = Song.objects.get(pk=pk)
    song.delete()
    return redirect('songs:index')
    