from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=20)
    artist = models.CharField(max_length=20)
    description = models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)