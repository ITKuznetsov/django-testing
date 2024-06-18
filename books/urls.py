from django.urls import path

from books import views

app_name = 'books'

urlpatterns = [
    path('api/v1/bookslist', views.BooksAPIView.as_view(), name='BooksAPIv1'),
]