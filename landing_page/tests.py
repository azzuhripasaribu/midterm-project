from django.test import TestCase
from django.test import LiveServerTestCase, TestCase, tag
from django.urls import reverse

class MainTestCase(TestCase):
    def test_root_url_status_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # You can also use path names instead of explicit paths.
        response = self.client.get(reverse('landing_page:home'))
        self.assertEqual(response.status_code, 200)

