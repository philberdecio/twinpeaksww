from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=100, blank = False)
    img = models.CharField(max_length=250, blank = False)
    aka = models.CharField(max_length=100, blank = True)
    bio = models.TextField(max_length=500, blank = False)
    see_also = models.CharField(max_length=200, blank = True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
