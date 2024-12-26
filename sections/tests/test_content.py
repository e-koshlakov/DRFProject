import os

from rest_framework.test import APITestCase
from rest_framework import status

from sections.models import Section, SectionContent
from users.tests.utils import get_admin_user
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


class ContentTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = get_admin_user()
        response = self.client.post('/api/v1/users/token/', {"email": "tester@web.top", "password": "Qwerty12"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.test_section = Section.objects.create(
            title='test_section',
            description='test_description'
        )
        self.test_content = SectionContent.objects.create(
            section=self.test_section,
            title='test_content_title',
            content='test_content_content'
        )

    def test_content_create(self):
        data = {
            'section': 1,
            'title': 'test_content_create',
            'content': 'test_content_description_create',
        }
        response = self.client.post('/api/v1/content/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['title'], 'test_content_create')

    def test_content_delete(self):
        response = self.client.delete(f'/api/v1/content/{self.test_content.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_content_detail(self):
        response = self.client.get(f'/api/v1/content/{self.test_content.id}/')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['title'], 'test_content_title')
        self.assertEqual(response.json()['content'], 'test_content_content')
        self.assertEqual(self.test_content.__str__(), 'test_content_title')

    def test_content_list(self):
        response = self.client.get('/api/v1/content/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['results'][0]['title'], 'test_content_title')

    def test_content_update(self):
        data = {
            'section': self.test_section.id,
            'title': 'test_content_put',
            'content': 'test_content_description_put',
        }
        response = self.client.put(f'/api/v1/content/{self.test_content.id}/update/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['section'], self.test_section.id)
        self.assertEqual(response.json()['title'], 'test_content_put')
        self.assertEqual(response.json()['content'], 'test_content_description_put')
