class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self,name,pet_type,owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self,pet_type):
        if pet_type in Pet.PET_TYPES:
            self._pet_type = pet_type
        else:
            raise Exception('The pet type must be in the approved list')

class Owner:
    def __init__(self,name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self,pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise ValueError('The pet must be an instance of the Pet class.')

    def get_sorted_pets(self):
        owners_pets = Owner.pets(self)
        return sorted(owners_pets, key=lambda pet: pet.name)

