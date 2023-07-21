from django.shortcuts import render
from app1.serializers import AuthorSerializer, BookSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from app1.models import Author, Book

# Create your views here.
class AuthorView1(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorView2(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookView1(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookView2(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
