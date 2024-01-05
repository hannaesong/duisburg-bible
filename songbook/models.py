from django.db import models
from django.urls import reverse

class Song(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})