from django.test import TestCase
from django.urls import resolve
from .views import home_page


class HomepageTest(TestCase):

    def test_url_root_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
