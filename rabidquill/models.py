from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


# Create your models here.
class Directory(models.Model):
    name = models.TextField(max_length=25)
    author = models.ForeignKey(User)
    created = models.DateTimeField()
    modified = models.DateTimeField()

class DirectoryParents(models.Model):
    parent = models.ForeignKey(Directory)

class Document(models.Model):
    title = models.TextField(max_length=250)
    author = models.ForeignKey(User)
    body = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    directory = models.ForeignKey(Directory)

admin.site.register(Directory)
admin.site.register(DirectoryParents)
admin.site.register(Document)