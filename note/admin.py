from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ("date", "author",)
    prepopulated_fields = {"slug": ("date", "author",)}
admin.site.register(Note)