from abc import ABCMeta, abstractmethod
class Ingredient(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def add(self):
        pass


class ThinCrustDough(Ingredient):
    def add(self):
        print('Preparing with thin crust dough.')

class ThickCrustDough():
    def add(self):
        print('Preparing with think crust dough.')

class MarineraSauce():
   def add(self):
    print('Preparing with Marinera Sauce.')

class PlumTomatoSauce():
    def add(self):
        print('Preparing with Plum Tomato Sauce.')

class ReggianoCheese():
    def add(self):
        print('Sprinkling Reggiano Cheese on top.')

class MozzarellaCheese():
    def add(self):
        print('Sprinkling Mozzarella Cheese on top.')

class Garlic():
    def add(self):
        print('Adding garlic topping.')

class Onion():
    def add(self):
        print('Adding onion topping.')

class Mushroom():
    def add(self):
        print('Adding mushroom topping.') 

class RedPepper():
    def add(self):
        print('Adding red pepper topping.')

class Eggplant():
    def add(self):
        print('Adding eggplant topping.')

class Spinach():
    def add(self):
        print('Adding spinach topping.')

class BlackOlives():
    def add(self):
        print('Adding black olives topping.')

class SlicedPepperoni():
    def add(self):
        print('Adding sliced pepperoni topping.')