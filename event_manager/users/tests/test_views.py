from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.models import User

class UserRegisterTest(TestCase):
   
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
           
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')
        

class UserLoginTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
           
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

class UserLogoutTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
           
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/logout.html')       