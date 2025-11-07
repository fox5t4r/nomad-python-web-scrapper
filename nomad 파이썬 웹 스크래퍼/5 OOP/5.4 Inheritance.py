class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

class GuardDog(Dog):
    def rrrr(self):
        print('stay away!')

class Puppy(Dog):
    def __str__(self):
        return f'{self.breed} puppy named {self.name}'
    
    def woof(self):
        print('woof woof!')

Tom = Puppy(
    name='Tom', 
    breed='beegle',
    age=0.1
    )
bibi = Puppy(
    name='bibi', 
    breed='dalmatian',
    age=5
    )

print(
    Tom,
    bibi
)