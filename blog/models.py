""" blog/models.py
    By Luferat
"""

from django.contrib.auth.models import User
from django.db import models
from django.db.models.expressions import F
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


class Comment(models.Model):
    
    STATUS = (
        ('Ativo', 'ativo'),
        ('Moderando', 'moderando'),
        ('Inativo', 'inativo'),
    )

    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    author = models.CharField(max_length=255, blank=False)
    comment = models.TextField()
    status = models.CharField(choices=STATUS, max_length=10, default='Moderando')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author;