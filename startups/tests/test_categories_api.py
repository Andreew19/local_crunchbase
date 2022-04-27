from django.test import TestCase
from rest_framework.test import APIClient

from startups.models import Categories

class CategoriesApiTestCase(TestCase):
    def setUp(self):
      Categories.objects.create(name="Crypto")

    def test_list(self):
        factory = APIClient()

        response = factory.get('/srv/api/v1/categories/')
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.data[0]['name'], 'Crypto')
        self.assertEqual(response.data[0]['id'], 1)

    def test_create(self):
        factory = APIClient()

        response = factory.post('/srv/api/v1/categories/', { 'name': 'Ecommerce' })
        self.assertEqual(201, response.status_code)

        response = factory.get('/srv/api/v1/categories/')
        self.assertEqual(response.data[1]['name'], 'Ecommerce')
        self.assertEqual(response.data[1]['id'], 2)
