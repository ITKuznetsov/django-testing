from django.db import models

from books.utils import AbstractModel

class Author(AbstractModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Book(AbstractModel):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title
