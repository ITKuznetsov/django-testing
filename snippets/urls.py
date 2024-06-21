from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

appname = 'snippets'

urlpatterns = [
    path('', views.snippet_list),
    path('<int:pk>/', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)