class Pet:
    def __init__(self,name,species,vaccinated=False):
        self.name = name
        self.species = species
        self.vaccinated = vaccinated


dog = Pet('Buddy','Dog',True)
print(dog.vaccinated)