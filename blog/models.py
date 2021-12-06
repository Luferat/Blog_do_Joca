""" blog/models.py
    By Luferat
"""

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Modelo das postagens do blog


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Ordena do mais recente para o mais antigo
    class Meta:
        ordering = ('-created',)

    # Usa o valor de 'title' para listar posts pelo Django Admin
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def get_home(self):
        return reverse('blog:list')
