from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from posts.models import Post

# Create your models here.


class Comment(models.Model):
    """create model for blogs."""
    id = models.AutoField(primary_key=True)
    message = models.TextField(max_length=4000)
    post = models.ForeignKey(Post, default=1)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    path = ArrayField(models.IntegerField(blank=True, editable=False))
    depth = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ["-date_created", "-date_updated"]

    # def get_absolute_url(self):
    #     return reverse("posts:post_detail", kwargs={"slug": self.slug})
