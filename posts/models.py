from django import forms
from django.db import models
import random
import string
# Create your models here.


class User(models.Model):
    """create model for users."""

    full_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField()
    password = models.CharField(max_length=100, blank=False)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.email


class Post(models.Model):
    """create model for blogs."""
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField(max_length=4000)
    author = models.CharField(max_length=400, default="doe")
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    slug = models.SlugField(null=False, unique=True, max_length=100)

    def __str__(self):
        return self.title
