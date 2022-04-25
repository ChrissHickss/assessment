from django.contrib import admin
from .models import Category, Post
# Register your models here.

my_models = [Category, Post]

admin.site.register(my_models)