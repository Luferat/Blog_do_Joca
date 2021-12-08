""" contact/admin.py
    By Luferat
"""

from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    # Lista de campos para exibição da lista de posts
    list_display = ('name', 'email', 'subject')
