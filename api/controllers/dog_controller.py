from typing import Any, Dict

from pydantic import BaseModel
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.models import Dog
from api.serializers import DogSerializer
from api.services import DogService


class CreateDogDto(BaseModel):
    """
    This is the data transfer object for the creation of a dog action.
    """

    name: str
    breed: str
    age: int


class DogController(viewsets.ModelViewSet):
    """
    Endpoints for the dog Model:
    """

    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    permission_classes = [AllowAny]

    def __init__(self):
        super().__init__()
        self.dog_service = DogService()

    @action(detail=False, methods=["get"])
    def young_dogs(self):
        young_dogs = self.dog_service.get_young_dogs()
        serializer = self.get_serializer(young_dogs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def get_dog(self):
        print("get_dog")
        return Response(200)

    @action(detail=False, methods=["post"])
    def create_dog(self, request: CreateDogDto):
        dog_data: Dict[str, Any] = request.data.get("data", {})
        new_dog = Dog.objects.create(
            name=dog_data.get("name"),
            breed=dog_data.get("breed"),
            age=dog_data.get("age"),
        )
        new_dog.save()

        all_dogs = self.dog_service.get_all_dogs()
        all_dogs.filter(name___asdfasdfasdfcce="asdf")
        print(all_dogs)
        serializer = self.get_serializer(new_dog)
        return Response(serializer.data, status=200)

    @action(detail=False, methods=["post"])
    def print_dog_created(self, request: CreateDogDto) -> Response:
        create_dog_dto: CreateDogDto = request

        dog_data: Dict[str, Any] = request.data.get("data", {})
        new_dog = Dog.objects.create(
            name=dog_data.get("name", "Unknown"),
            breed=dog_data.get("breed"),
            age=dog_data.get("age", 0),
        )

        old_dog = Dog.objects.create()
        print(f"new_dog: ${new_dog}")
        print(f"old_dog: ${old_dog}")
        serializer = self.get_serializer(new_dog)
        return Response(serializer.data, status=201)
