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
        response = self.client.post('/users/token/', {"email":"test_member@web.top", "password":"qwerty"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')


    def test_user_create(self):
        data = {
            # "username": "test_user",
            "email": "test_member_1@web.top",
            "role": 'member',
            "password": 'qwerty',
        }
        response = self.client.post('/users/create/', data, format='json')

        # print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['email'], 'test_member_1@web.top')

    def test_users_delete(self):
        response = self.client.delete(f'/users/{self.user.id}/delete/')
        # response = self.client.post(reverse('user-delete', kwargs={'pk': 3}))

        # print(response)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_users_detail(self):
        response = self.client.get(f'/users/{self.user.id}/')
        print(response.json())
        # response = self.client.get(reverse('user-detail', kwargs={'pk': 4}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['email'], 'test_member@web.top')
        self.assertEqual(response.json()['is_active'],True)

    def test_users_list(self):
        response = self.client.get('/users/')
        # response = self.client.get(reverse('user-list'))
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[0]['email'], 'test_member@web.top')

    def test_user_update(self):
        data = {
            "email": "test_member_update@web.top",
            "password": 'qwerty',

        }
        response = self.client.patch(f'/users/{self.user.id}/update/', data=data)
        print(response.json())
        # response = self.client.patch(reverse('user-update', kwargs={'pk': 5}), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['email'], "test_member_update@web.top")
