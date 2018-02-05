from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.http import HttpRequest
# from django_downloadview import setup_view

# from django.test import TestCase
from posts.views import PostView


class PageTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
        username='jacob', email='jacob@…', password='top_secret')

    def setup_view(view, request, *args, **kwargs):
        """Mimic ``as_view()``, but returns view instance.
        Use this function to get view instances on which you can run unit tests,
        by testing specific methods."""

        view.request = request
        view.args = args
        view.kwargs = kwargs
        return view

    def test_root_url_resolves_to_home_page_view(self):
        request = self.factory.get('/')
        request.user = self.user

        with self.assertTemplateUsed(template_name='posts.html'):
            response = PostView.as_view()(request)
            self.assertEqual(response.status_code, 200)


    def test_home_page_returns_correct_html(self):
        request = self.factory.get('/')
        request.user = self.user
        view = PostView.as_view(template_name='posts.html')
        with self.assertTemplateUsed(template_name='posts.html'):
            response = view(request, name='posts')
            html = response.content.decode('utf8')
            expected_html = render_to_string('posts.html')
            self.assertTrue(html.strip().startswith('<!DOCTYPE html>'))
            self.assertIn('<title>Posts | Django Creek</title>', html)
            self.assertTrue(html.strip().endswith('</html>'))
