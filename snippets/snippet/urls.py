from django.contrib import admin
from django.urls import path, include
from snippet.views import snippet_list, snippet_detail, SnippetDetail, SnippetList

urlpatterns = [
    path('snippets/', SnippetList.as_view()),
    path('snippet/<int:pk>/', SnippetDetail.as_view()),
]
