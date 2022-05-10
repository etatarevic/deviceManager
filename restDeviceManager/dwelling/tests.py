from django.db import IntegrityError
from django.test import TestCase
from hub.models.hub import Hub
from .models.location import Location
from .models.dwelling import Dwelling

class TestAPI(TestCase):
    def setUp(self):
        self.location = Location.objects.create(street="123 ABC Street")
        self.hub = Hub.objects.create(name="Hub")
        self.dwelling = Dwelling.objects.create(
            name="d1", 
            location=self.location, 
            is_occupied=True, 
            installed_hub=self.hub
        )

    def test_create_non_unique_dwelling(self):
        with self.assertRaises(IntegrityError):
            Dwelling.objects.create(
                name="d1", 
                location=self.location, 
                is_occupied=True, 
                installed_hub=self.hub
            )

    def test_create_unique_dwelling(self):
        d1 = Dwelling.objects.create(
            name="d1", 
            location=Location.objects.create(street="123 Main Street"), 
            is_occupied=True, 
            installed_hub=Hub.objects.create(name="Hub1")
        )
        self.assertIsNotNone(d1)

    def test_update_dwelling(self):
        self.dwelling.name = "d1 updated"
        self.dwelling.save()
        self.dwelling.refresh_from_db()
        self.assertEqual(self.dwelling.name, "d1 updated")

    def test_remove_dwelling(self):
        d1 = Dwelling.objects.create(
            name="d1", 
            location=Location.objects.create(street="123 Main Street"), 
            is_occupied=True, 
            installed_hub=Hub.objects.create(name="Hub1")
        )
        self.assertEqual(Dwelling.objects.count(), 2)
        d1.delete()
        self.assertEqual(Dwelling.objects.count(), 1)
