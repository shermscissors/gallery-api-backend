from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.title