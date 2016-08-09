from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    
    title = models.CharField(max_length=300)
    author= models.CharField(max_length=200, blank=True)
    edition= models.CharField(max_length=100, blank= True)
    publisher =models.CharField(max_length=200,blank= True)
    publishing_year = models.CharField(max_length=100, blank= True)
    category= models.CharField(max_length=150,blank= True)
    ISBN = models.CharField(max_length=200,blank= True)
    online_stores = models.CharField(max_length=500, blank=True)
    
    
    
    
    
    def __str__(self):
        return "Title" , self.title
    