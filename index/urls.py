from django.urls import path

from . import views

appname = 'index'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]