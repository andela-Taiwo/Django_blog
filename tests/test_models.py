from django.test import TestCase
from posts.models import Post
from django.utils import timezone
from django.contrib.auth.models import User


class PostModelTest(TestCase):

    def setUp(self):
        first_name = "only"
        last_name = "test"
        username = '@onlytest'
        email = "test@gmail.com"
        password = "123444"
        User.objects.create(first_name=first_name,
                            last_name=last_name,
                            email=email, password=password,
                            username=username)

    def test_user_creation(self):
        user = User.objects.get(email="test@gmail.com")
        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.__str__(), str(user.username))


class ModelTest(TestCase):

    def setUp(self):
        first_name = "only"
        last_name = "test"
        username = '@onlytest'
        email = "test@gmail.com"
        password = "123444"
        User.objects.create(first_name=first_name,
                            last_name=last_name,
                            email=email, password=password,
                            username=username)
        title = "Learning Django"
        content = "The real aspect of Django \n it is actually cool"
        Post.objects.create(title=title, content=content,
                            date_created=timezone.now(),
                            date_updated=timezone.now(),
                            user_id=User.objects.get(id=1))

    def test_post_creation(self):
        post = Post.objects.get(title="Learning Django")
        self.assertTrue(isinstance(post, Post))
        self.assertEqual(post.__str__(), post.title)
