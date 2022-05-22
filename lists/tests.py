from django.urls import resolve
from django.test import TestCase

from lists.views import home_page


# Create your tests here.
class HomePageTest(TestCase):
    """ Test suite for home_page view """

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
