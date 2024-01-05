from django.shortcuts import render, get_object_or_404
from .models import Song

def allsongs(request):
    songs = Song.objects.all().order_by('title').values()
    return render(request, 'songbook/allsongs.html', {'songs':songs})

def detail(request, slug):
    song = get_object_or_404(Song, slug=slug)
    return render(request, 'songbook/detail.html', {'song':song})