""" blog/admin.py
    By Luferat
"""

from django.contrib import admin

# Register your models here.
from .models import Post

# admin.site.register(Post) --> Substituído pelas linahs abaixo

# Formata posts no Django Admin


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    # Lista de campos para exibição da lista de posts
    list_display = ('title', 'slug', 'author', 'created', 'updated')

    # Preenche o campo 'slug' automaticamente ao criar um post
    prepopulated_fields = {'slug': ('title',)}
