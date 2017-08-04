from abc import ABCMeta, abstractmethod
from Ingredients import (ThinCrustDough, ThickCrustDough, MarineraSauce, PlumTomatoSauce, ReggianoCheese, MozzarellaCheese, 
    Garlic, Onion, Mushroom, RedPepper, Eggplant, Spinach, BlackOlives, SlicedPepperoni)

class PizzaIngredientFactory(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_dough(self):
        pass
    
    @abstractmethod
    def create_sauce(self):
        pass
    
    @abstractmethod
    def create_cheese(self):
        pass
    
    @abstractmethod
    def create_veggies(self):
        pass
    
    @abstractmethod
    def create_pepperoni(self):
        pass


class NYIngredientFactory(PizzaIngredientFactory):
    def __init__(self):
        pass

    def create_dough(self):
        thin_crust_dough = ThinCrustDough()
        thin_crust_dough.add()
        return thin_crust_dough

    def create_sauce(self):
        marinera_sauce = MarineraSauce()
        marinera_sauce.add()
        return marinera_sauce

    def create_cheese(self):
        reggiano_cheese = ReggianoCheese()
        reggiano_cheese.add()
        return reggiano_cheese

    def create_veggies(self):
        garlic = Garlic()
        onion = Onion()
        mushroom = Mushroom()
        red_pepper = RedPepper()
        return [garlic.add(), onion.add(), mushroom.add(), red_pepper.add()]

    def create_pepperoni(self):
        sliced_pepperoni = SlicedPepperoni()
        sliced_pepperoni.add()
        return sliced_pepperoni

class ChicagoIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        thick_crust_dough = ThickCrustDough()
        thick_crust_dough.add()
        return thick_crust_dough

    def create_sauce(self):
        plum_tomato_sauce = PlumTomatoSauce()
        plum_tomato_sauce.add()
        return plum_tomato_sauce

    def create_cheese(self):
        mozarella_cheese = MozzarellaCheese()
        mozarella_cheese.add()
        return mozarella_cheese

    def create_veggies(self):
        eggplant = Eggplant()
        spinach = Spinach()
        black_olives = BlackOlives()
        return [eggplant.add(), spinach.add(), black_olives.add()]

    def create_pepperoni(self):
        sliced_pepperoni = SlicedPepperoni()
        sliced_pepperoni.add()
        return sliced_pepperoni