from django.urls import resolve
from django.test import TestCase

from lists.views import home_page


# Create your tests here.
class HomePageTest(TestCase):
    """ Test suite for home_page view """

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
