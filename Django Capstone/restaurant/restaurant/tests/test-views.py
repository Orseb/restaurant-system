from django.test import TestCase
from ..models import Menu

class MenuViewTest(TestCase):
    def setup(self):
        item = Menu.objects.create(Title='IceCream', Price=80, Inventory=100)
    
    def test_getall(self):
        all_objects = Menu.objects.all()
        self.assertEqual(all_objects, all_objects)
