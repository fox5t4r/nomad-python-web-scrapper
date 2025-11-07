class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def sleep(self):
        print('zzzzz....')

class GuardDog(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed, 5)

    def rrrr(self):
        print('stay away!')

class Puppy(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed, 0.1)
    
    def woof(self):
        print('woof woof!')

Tom = Puppy(
    name='Tom', 
    breed='beegle'
    )
bibi = GuardDog(
    name='bibi', 
    breed='dalmatian'
    )

Tom.woof()
Tom.sleep()
bibi.rrrr()
bibi.sleep()