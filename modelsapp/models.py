import datetime
from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100000,default='')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True,blank=True)
    
    def __str__(self):
        return self.title
