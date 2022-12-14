from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=100, blank = False)
    img = models.CharField(max_length=250, blank = False)
    aka = models.CharField(max_length=100, blank = True)
    bio = models.TextField(max_length=500, blank = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Quote(models.Model):

    quote = models.TextField(max_length=500, blank = False)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name="quotes")

    def __str__(self):
        return self.quote

class Quotelist(models.Model):

    title = models.CharField(max_length=150)
    # this is going to create the many to many relationship and join table
    quotes = models.ManyToManyField(Quote)

    def __str__(self):
        return self.title

