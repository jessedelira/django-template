from django.db import models


class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f"Dog\n name: {self.name}\nbreed: {self.breed}\nage: {self.age}"
