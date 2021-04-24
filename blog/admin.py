from django.contrib import admin
from .models import Categorie, Comment, Post, Profile

# Register your models here.
admin.site.register(Post)
admin.site.register(Categorie)
admin.site.register(Profile)
admin.site.register(Comment)