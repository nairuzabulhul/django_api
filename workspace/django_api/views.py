from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404 
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status

from serializers import BookSerializer
from .models import Book


# Create your views here.
class BookList(APIView):
    
    #GET 
    def get(self,request):
        
        books = Book.objects.all()  #return all the data form 
        serializers = BookSerializer(books, many=True) # serialize the data 
        return Response (serializers.data) # return data in a form of JSON
        
    
    #POST
    def post(self,request, format=None):
        
        serializers = BookSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    

# Detailed BookDetail
class BookDetail(APIView):
    
    
    def get_object(self,pk):
    
        try:
            return Book.objects.get(pk=pk)
            
        except Book.DoesNotExist:
            raise Http404
    
    #GET
    def get(self, request, pk, format=None):
        
        books = self.get_object(pk)
        serializers = BookSerializer(books)
        return Response(serializers.data)
        
    
    #UPDATE
    def put(self,request, pk,format=None):
        
        books = self.get_object(pk) # get the primary key of the entry from the database
        serializers = BookSerializer(books, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    #Delete
    def delete(self,request,pk,format=None):
        
        books = self.get_object(pk)
        books.delete() # remove the entry  
