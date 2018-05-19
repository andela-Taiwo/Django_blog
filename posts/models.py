from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db.models.signals import pre_save, post_save
from django.db.models.signals import post_save as signals_post_save
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from notifications.signals import notify

from django.db import models
# from django.contrib.auth.models import User

# Create your models here.


def upload_location(instance, filename):
    PostModel = instance.__class__
    posts = PostModel.objects.all()
    if posts:
        new_id = PostModel.objects.order_by("id").last().id + 1
        return "%s/%s" % (new_id, filename)

    new_id = 1
    return "%s/%s" % (new_id, filename)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    objects = UserManager()
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=32, default='John', blank=False)
    last_name = models.CharField(max_length=32, default='Doe', blank=False)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser
    # notice the absence of a "Password field", that's built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & Password are required by default.

    def get_full_name(self):
    # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active



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
