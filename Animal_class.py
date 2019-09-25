class Animal():
# a class the blueprint for making instances
    # Characteristics - instances refer to characteristics

    def __init__(self, name, colour, eyes =2): #runs only once when you initialise an object. Default at end.
        self.name = name
        self.number_eyes = eyes
        self.alive = True
        self.number_animals_eaten = 0
        self.age = 0
        self.colour = colour

    # Behaviours - functions that belong to a class.
    # Methods - functions that can only be used on this class instance.

    def eat(self, food = 'Fajitas'): # making an argument optional.
        return 'NOM NOM NOM ' +  food

    def sleep(self):
        return 'zzzzzzzzzzzzzzzzzzzzzzzz zz soooooo sleeeeeeppppy'

    def hunt(self):
        return 'ATTTTTAAACCCKKK!! THIS IS SPARTA!!!!!'

    def potty(self):
        return 'O_O ... HUNN o_O ---- HUUHH!! O_O SPOSH! -.- :D'

    def roar(self):
        return 'RRRRRRRRRRRRROOOOOOOOOOOOOAAAAAAAAAAAAARRRRRRRR!!!'

 # Let's create an object of class animal :)
    # Initializing an object

# my_animal = Animal() # This is where I created an instance of class Animal
#
# print(my_animal)
# print(type(my_animal))

# Main is where it is ran from.