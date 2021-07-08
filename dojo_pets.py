from Pet import Pet

class ninja:

    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk (self):
        self.pet.play()

    def feed(self):
        self.pet.eat()

    def bathe(self):
        print(f"You bathe {self.pet.name}")
        self.pet.noise()


sparky = Pet('Sparky', 'Dog', 'Fetch', 100, 100)
alex = ninja('Alex', 'Santana', 'cookies', 'bones', sparky )

alex.feed()
alex.walk()
alex.bathe()