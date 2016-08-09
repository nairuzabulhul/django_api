from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ['pk','title','author','edition','publisher','publishing_year','category','ISBN']
