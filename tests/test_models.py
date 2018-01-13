from django.test import TestCase
from posts.models import User, Post
from django.utils import timezone


class UserModelTest(TestCase):

    def setUp(self):
        full_name = "only test"
        email = "test@gmail.com"
        password = "123444"
        User.objects.create(full_name=full_name,
                            email=email, password=password,
                            date_created=timezone.now(),
                            date_updated=timezone.now())

    def test_user_creation(self):
        user = User.objects.get(email="test@gmail.com")
        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.__str__(), str(user.email))


class ModelTest(TestCase):

    def setUp(self):
        full_name = "only test"
        email = "test@gmail.com"
        password = "123444"
        User.objects.create(full_name=full_name,
                            email=email, password=password,
                            date_created=timezone.now(),
                            date_updated=timezone.now())
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
