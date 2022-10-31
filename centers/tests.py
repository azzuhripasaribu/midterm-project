from django.test import TestCase

# Create your tests here.

from django.test import TestCase, Client
from django.urls import reverse, resolve
# from django.contrib.auth import get_user_model
from centers.views import find_centers, add_center, find_centers_JSON, get_areas_JSON

# Create your tests here.
class TestUrls(TestCase):
    def test_find_centers_url_is_resolved(self):
        url = reverse('centers:main')
        self.assertEqual(resolve(url).func, find_centers)
    
    def test_find_centers_JSON_url_is_resolved(self):
        url = reverse('centers:json')
        self.assertEqual(resolve(url).func, find_centers_JSON)
    
    def test_add_center_url_is_resolved(self):
        url = reverse('centers:add')
        self.assertEqual(resolve(url).func, add_center)

    # def test_get_area_JSON_url_is_resolved(self):
    #     url = reverse('centers:areajson')
    #     self.assertEqual(resolve(url).func, get_areas_JSON)


class TestViews(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.main_url = reverse('centers:main')
        self.add_center_url = reverse('centers:add')
        self.json_url = reverse('centers:json')
        self.area_json_url = reverse('centers:areajson')


    def test_find_centers_view(self):
        response = self.client.get(self.main_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'findCenters.html')

    def test_find_centers_json_view(self):
        response = self.client.get(self.json_url)

        self.assertEqual(response.status_code, 200)

    def test_get_area_json_view(self):
        response = self.client.get(self.area_json_url)

        self.assertEqual(response.status_code, 200)

    def test_add_center_views_GET(self):
        response = self.client.get(self.add_center_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'addCenter.html')

    def test_add_center_views_POST(self):
        response = self.client.post(self.add_center_url, data={
            'name':'Realfo und Ation',
            'website':'HTTPS://realfo.com/',
            'email':'contact@realfo.ua',
            'areas':'Gdansk'
        })

        self.assertEqual(response.status_code, 302)
