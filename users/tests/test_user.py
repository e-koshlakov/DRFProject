import os
import django
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from users.tests.utils import get_admin_user

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


class UserTestCase(APITestCase):
    """
    ОБЩИЙ для запуска тестов из терминала
    """

    def setUp(self) -> None:
        """Базовые настройки"""
        self.user = get_admin_user()
        response = self.client.post('/api/v1/users/token/', {"email": "tester@web.top", "password": "Qwerty12"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')


    def test_user_create(self):
        data = {
            "email": "test_member_1@web.top",
            "role": 'member',
            "password": 'Qwerty12',
        }
        response = self.client.post('/api/v1/users/create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['email'], 'test_member_1@web.top')

    def test_users_delete(self):
        response = self.client.delete(f'/api/v1/users/delete/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_users_detail(self):
        response = self.client.get(f'/api/v1/users/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['email'], 'tester@web.top')
        self.assertEqual(response.json()['is_active'], True)

    def test_users_list(self):
        response = self.client.get('/api/v1/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[0]['email'], 'tester@web.top')

    def test_user_update(self):
        data = {
            "email": "tester_update@web.top",
            "password": 'Qwerty12',

        }
        response = self.client.patch(f'/api/v1/users/update/{self.user.id}/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['email'], "tester_update@web.top")
