from abc import ABCMeta, abstractmethod
class Ingredient(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def add(self):
        pass


class ThinCrustDough(Ingredient):
    def add(self):
        print('Preparing with thin crust dough.')

class ThickCrustDough(Ingredient):
    def add(self):
        print('Preparing with think crust dough.')

class MarineraSauce(Ingredient):
   def add(self):
    print('Preparing with Marinera Sauce.')

class PlumTomatoSauce(Ingredient):
    def add(self):
        print('Preparing with Plum Tomato Sauce.')

class ReggianoCheese(Ingredient):
    def add(self):
        print('Sprinkling Reggiano Cheese on top.')

class MozzarellaCheese(Ingredient):
    def add(self):
        print('Sprinkling Mozzarella Cheese on top.')

class Garlic(Ingredient):
    def add(self):
        print('Adding garlic topping.')

class Onion(Ingredient):
    def add(self):
        print('Adding onion topping.')

class Mushroom(Ingredient):
    def add(self):
        print('Adding mushroom topping.') 

class RedPepper(Ingredient):
    def add(self):
        print('Adding red pepper topping.')

class Eggplant(Ingredient):
    def add(self):
        print('Adding eggplant topping.')

class Spinach(Ingredient):
    def add(self):
        print('Adding spinach topping.')

class BlackOlives(Ingredient):
    def add(self):
        print('Adding black olives topping.')

class SlicedPepperoni(Ingredient):
    def add(self):
        print('Adding sliced pepperoni topping.')