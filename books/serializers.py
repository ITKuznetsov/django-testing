import io
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from books.models import Book


# class BooksModel:
#     def __init__(self, title, description) -> None:
#         self.title = title
#         self.description = description


# class BooksSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     description = serializers.CharField()
#     author = serializers.StringRelatedField(source='author.name')
#     price = serializers.DecimalField(max_digits=6, decimal_places=2)

# def encode():
#     model = BooksModel('Kniga', 'SuperKniga')
#     model_sr = BooksSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)

# def decode():
#     stream = io.BytesIO(b'{"title":"Kniga","description":"SuperKniga"}')
#     data = JSONParser().parse(stream)
#     serializer = BooksSerializer(data=data)
#     serializer.is_valid()
#     if serializer.is_valid():
#         print(serializer.validated_data)
#     else:
#         print(serializer.errors)

class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'