from api.models.dog import Dog


class DogService:
    def __init__(self):
        # You could inject dependencies here if needed
        pass

    def get_young_dogs(self):
        return Dog.objects.filter(age__lt=3)

    def calculate_human_age(self, dog):
        return dog.age * 7

    def get_all_dogs(self):
        return Dog.objects.all()
