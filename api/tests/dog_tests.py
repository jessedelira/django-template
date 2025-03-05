from django.test import TestCase

from api.models import Dog


class DogModelTests(TestCase):
    def test_dog_creation(self):
        dog = Dog.objects.create(name="Buddy", breed="Labrador", age=3)
        self.assertEqual(dog.name, "Buddy")
