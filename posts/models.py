from django.db import models

# Create your models here.


class User(models.Model):
    """create model for users."""

    full_name = models.CharField(max_length=50, blank=False)
    email = models.CharField(max_length=50, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.email


class Blog(models.Model):
    """create model for blogs."""

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=400)
    date_created = models.DateField()
    date_updated = models.DateField()
