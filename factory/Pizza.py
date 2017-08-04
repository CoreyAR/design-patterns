from abc import ABCMeta, abstractmethod

class Pizza(object):
    __metaclass__ = ABCMeta
    def __init__(self):
        self.name = ''

    @abstractmethod
    def prepare(self):
        pass
    
    def bake(self):
        print("Bake for 25 minutes at 350 degrees")
    
    def cut(self):
        print("Cutting the pizza into diagonal slices")
    
    def box(self):
        print("Place pizza in official PizzaStore box")

    def set_name(self, name):
        self.name = name
    

class CheesePizza(Pizza):
    def __init__(self, ingredientFactory):
        self.ingredientFactory = ingredientFactory
        self.dough = None
        self.sauce = None
        self.cheese = None
        self.toppings = None
    
    def prepare(self):
        self.dough = self.ingredientFactory.create_dough()
        self.sauce = self.ingredientFactory.create_sauce()
        self.cheese = self.ingredientFactory.create_cheese()


class PepperoniPizza(Pizza):
    def __init__(self, ingredientFactory):
        self.ingredientFactory = ingredientFactory
        self.dough = None
        self.sauce = None
        self.cheese = None
        self.toppings = None
    
    def prepare(self):
        self.dough = self.ingredientFactory.create_dough()
        self.sauce = self.ingredientFactory.create_sauce()
        self.cheese = self.ingredientFactory.create_cheese()
        self.toppings = [self.ingredientFactory.create_pepperoni()]

class VeggiePizza(Pizza):
    def __init__(self, ingredientFactory):
        self.ingredientFactory = ingredientFactory
        self.dough = None
        self.sauce = None
        self.cheese = None
        self.toppings = None
    
    def prepare(self):
        self.dough = self.ingredientFactory.create_dough()
        self.sauce = self.ingredientFactory.create_sauce()
        self.cheese = self.ingredientFactory.create_cheese()
        self.toppings = self.ingredientFactory.create_veggies()
