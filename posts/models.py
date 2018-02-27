from django.db.models.signals import pre_save, post_save
from django.db.models.signals import post_save as signals_post_save
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from notifications.signals import notify

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


def upload_location(instance, filename):
    PostModel = instance.__class__
    posts = PostModel.objects.all()
    if posts:
        new_id = PostModel.objects.order_by("id").last().id + 1
        return "%s/%s" % (new_id, filename)

    new_id = 1
    return "%s/%s" % (new_id, filename)


class Post(models.Model):
    """create model for blogs."""
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField(max_length=4000)
    author = models.CharField(max_length=400, default="doe")
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    slug = models.SlugField(null=True, unique=True, max_length=100)
    publish = models.DateField(auto_now=True, null=True)
    blog_image = models.ImageField(upload_to=upload_location,
                                   null=True,
                                   blank=True,
                                   width_field="width_field",
                                   height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-date_created", "-date_updated"]

    def get_absolute_url(self):
        return reverse("posts:post_detail", kwargs={"slug": self.slug})


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Post)


class Profile(models.Model):
    "create model for users profile"
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    birth_date = models.DateField(auto_now=False, blank=True, null=True)
    picture = models.ImageField(upload_to=upload_location,
                                blank=True, null=True,
                                width_field="width_field",
                                height_field="height_field")
    height_field = models.IntegerField(default=0, null=True)
    width_field = models.IntegerField(default=0, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)


@receiver(signals_post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(signals_post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# 
# def my_handler(sender, instance, created, **kwargs):
#     notify.send(instance, verb='was saved')
#
#
# post_save.connect(my_handler, sender=Post)
