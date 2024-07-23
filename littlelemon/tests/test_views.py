from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=120, inventory=50)

    def test_getall(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)