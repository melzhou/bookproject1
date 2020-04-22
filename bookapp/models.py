from django.db import models

# Create your models here.

class book(models.Model):
    name = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    Excerpt = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.CharField(max_length = 200)

class writing(models.Model):
    name = models.CharField(max_length = 100)
    quote = models.TextField(null=True, blank=True)
    quotefrom = models.TextField(null=True, blank=True)
    source = models.TextField(null=True, blank=True)
    content = models.TextField()
