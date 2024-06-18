from django.urls import path

from books import views

urlpatterns = [
    path('api/v1/bookslist', views.BooksAPIView.as_view()),
]