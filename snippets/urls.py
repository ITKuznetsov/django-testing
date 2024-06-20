from django.urls import path

from . import views

appname = 'snippets'

urlpatterns = [
    path('', views.snippet_list),
    path('<int:pk>/', views.snippet_detail),
]