from django.shortcuts import render

from rest_framework import generics

from books.serializers import BooksSerializer
from .models import Book


class BooksAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
