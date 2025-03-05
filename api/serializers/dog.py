from rest_framework import serializers

from api.models.dog import Dog


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ["id", "name", "breed", "age"]
