from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    
     owner = serializers.ReadOnlyField(source='owner.username')

     class Meta:
        model = Book
        fields = ['pk','title','author','edition','publisher','publishing_year','category','ISBN','owner']
