from . import views
from django.urls import path, include

app_name = 'songbook'

urlpatterns = [
    path('', views.allsongs, name="allsongs"),
    path('<slug:slug>', views.detail, name='detail')
]