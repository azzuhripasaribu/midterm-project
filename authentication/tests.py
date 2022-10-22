from django.test import TestCase, Client
from django.urls import reverse, resolve


# Create your tests here.
class TestUrls(TestCase):
    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register)
        
    
    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, login)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logout)

class TestViews(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_register_GET(self):
        response = self.client.get(reverse('register'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_register_POST(self):
        response = self.client.post(reverse('register'), {
            'username':'JohnDoe',
            'password':'Example1.'
        })

        self.assertEqual(response.status_code, 302)
    
    def test_login_GET(self):
        self.client = Client(enforce_csrf_checks=True)
        response = self.client.get(reverse('login'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_POST(self):
        response = self.client.post(reverse('login'), {
            'username':'JohnDoe',
            'password':'Example1.'
        })

        self.assertEqual(response.status_code, 302)

    def test_logout(self):
        self.client.login(username='JohnDoe', password='Example1.')
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 302)
        
class TestForms(TestCase):
    pass