from django.contrib import admin
from django.urls import path, include
from snippet.views import snippet_list

urlpatterns = [
    path('snippet/', snippet_list)
]
