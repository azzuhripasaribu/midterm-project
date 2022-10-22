from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from authentication.views import register_user, login_user, logout_user


# Create your tests here.
class TestUrls(TestCase):
    def test_register_url_is_resolved(self):
        url = reverse('authentication:register')
        self.assertEqual(resolve(url).func, register_user)
        
    
    def test_login_url_is_resolved(self):
        url = reverse('authentication:login')
        self.assertEqual(resolve(url).func, login_user)

    def test_logout_url_is_resolved(self):
        url = reverse('authentication:logout')
        self.assertEqual(resolve(url).func, logout_user)

class TestViews(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.register_url = reverse('authentication:register')
        self.login_url = reverse('authentication:login')
        self.logout_url = reverse('authentication:logout')

    def test_register_GET(self):
        response = self.client.get(self.register_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_register_POST(self):
        response = self.client.post(self.register_url, data={
            'username':'JohnDoe',
            'password1':'Example1.',
            'password2':'Example1.'
        })

        self.assertEqual(response.status_code, 302)
    
    def test_login_GET(self):
        self.client = Client(enforce_csrf_checks=True)
        response = self.client.get(self.login_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_POST(self):
        UserModel = get_user_model()
        if not UserModel.objects.filter(username='JohnDoe').exists():
            user=UserModel.objects.create_user('JohnDoe', password='Example1.')
            user.save()
        response = self.client.post(self.login_url, data={
            'username':'JohnDoe',
            'password':'Example1.'
        })
        self.assertEqual(response.status_code, 302)

    def test_logout(self):
        self.client.login(username='JohnDoe', password='Example1.')
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)
        
class TestForms(TestCase):
    pass