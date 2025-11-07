class Puppy:
    def __init__(self, name, breed):
        self.name = name
        self.age = 1
        self.breed = breed

    def __str__(self):
        return f'{self.breed} puppy named {self.name}'
Tom = Puppy(
    name='Tom', 
    breed='beegle'
    )
bibi = Puppy(
    name='bibi', 
    breed='dalmatian'
    )

print(
    Tom,
    bibi
)