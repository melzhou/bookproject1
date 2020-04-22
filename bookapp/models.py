from django.db import models

# Create your models here.

class book(models.Model):
    name = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    description = models.TextField(null=True, blank=True)
    image = models.CharField(max_length = 200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class writing(models.Model):
    name = models.CharField(max_length = 100)
    quote = models.TextField(null=True, blank=True)
    quotefrom = models.TextField(null=True, blank=True)
    source = models.TextField(null=True, blank=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name