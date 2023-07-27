from django.test import TestCase

from restaurant.models import Menu


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)

    def test_getall(self):
        self.assertEqual(Menu.objects.all(), Menu.objects.all())
