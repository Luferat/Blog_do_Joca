""" blog/views.py
    By Luferat
"""

from django.views.generic import DetailView, ListView

from .models import Post

# View da lista de posts


class PostListView(ListView):
    model = Post


# View de um post completo


class PostDetailView(DetailView):
    model = Post
