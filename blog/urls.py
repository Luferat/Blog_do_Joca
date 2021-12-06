""" blog/urls.py
    By Luferat
"""

from typing import ValuesView
from django.urls import path

from . import views

# Namespace do aplicativo
app_name = 'blog'

# Rotas dos aplicativos
urlpatterns = [

    # Página inicial com a lista de posts
    path('', views.PostListView.as_view(), name='list'),

    # Exibe um post completo
    path('<slug:slug>/', views.PostDetailView.as_view(), name='detail'),
]
