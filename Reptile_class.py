from Animal_class import *

class Reptile(Animal): #Inheritance
    # It will run all the same method as Animal
    #Because that it all it knows.

    # def __init__(self):
    #     pass
    def __init__(self, name, colour, number_hearts, camo, eyes=2):
        super().__init__(name, colour, eyes) # Run the __init__ in parent class.
        self.number_h = number_hearts
        self.camo = camo
    # This above method overides the previous __init__ method. However,
    # the super call the previous init method so our object does have all of the previous characteristics.
    # AND THEN! we add more characteristics. 

    def eat(self, food = 'bugs'): # methods polymorphism where we override the method eat ()
        return "wait for it,... wait and pounce!! NOM bugs"

    def seek_heat(self): # adding new methods to this class  (polymorphing how the class looks)
        return 'Hmm bit chilly, where that sun at? why did I sit at the back of the class?'