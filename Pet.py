class Pet:

    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
        print(f"{self.name} sleeps and gains 25 energy\n Energy: {self.energy}")
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} eats gaining 10 health and 5 energy\n Health: {self.health}\n Energy: {self.energy}")
        return self

    def play(self):
        self.health += 5
        print(f"You play with {self.name}\n It gains 5 health.\n Health: {self.health}")
        return self

    def noise(self):
        if self.type == 'Dog':
            print('Woof!')
        if self.type == 'Cat':
            print('Meow!')
        if self.type == 'Bird':
            print('Chirp!')