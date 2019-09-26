from Animal_class import *
from Reptile_class import *

my_animal = Animal('Rick', 'Grey') # This is where I created an instance of class Animal
my_reptile = Reptile('Ringo', 'green', 2)
print(type(my_animal))
print(type(my_reptile))
print(my_animal.eat())
print(my_reptile.eat())
print(my_reptile.seek_heat())

# print(my_animal)
# print(type(my_animal))
# print(__name__)

# print(my_animal.eat('Lasagne'))
# print(my_animal.sleep())
# print(my_animal.potty())
# print(my_animal.name)

my_animal2 = Animal('Frank', 'Yellow')
# print(my_animal.eat('Lasagne'))
# print(my_animal.sleep())
# print(my_animal.potty())
# print(my_animal2.name)

my_animal3 = Animal('Stuart', 'White')
# print(my_animal.eat('Lasagne'))
# print(my_animal.sleep())
# print(my_animal.potty())
# print(my_animal3.name)
# print(my_animal3.number_eyes)
# print(my_animal3.colour)