from django.shortcuts import render, get_object_or_404
from .models import Note

def allnotes(request):
    notes = Note.objects.all()
    return render(request, 'note/allnotes.html', {'notes':notes})

def detail(request, slug):
    note = get_object_or_404(Note, slug=slug)
    return render(request, 'note/detail.html', {'note': note})