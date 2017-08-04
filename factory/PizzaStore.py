from abc import ABCMeta, abstractmethod
from PizzaIngredientFactory import NYIngredientFactory, ChicagoIngredientFactory
from Pizza import CheesePizza, PepperoniPizza, VeggiePizza

class PizzaStore(object):
    __metaclass__ = ABCMeta

    def order_pizza(self, pizza_type):
        pizza = self._create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    @abstractmethod
    def _create_pizza(self, pizza_type):
        pass



class NYPizzaStore(PizzaStore):
    def __init__(self):
        self.pizza = None

    def _create_pizza(self, pizza_type):
        ingredient_factory = NYIngredientFactory()
        if pizza_type == "cheese":
            self.pizza = CheesePizza(ingredient_factory)
            self.pizza.set_name("New York Style Cheese Pizza")
        elif pizza_type == "pepperoni":
            self.pizza = PepperoniPizza(ingredient_factory)
            self.pizza.set_name("Ney York Pepperoni Pizza")
        elif pizza_type == "veggie":
            self.pizza = VeggiePizza(ingredient_factory)
            self.pizza.set_name("Ney York Veggie Pizza")
        return self.pizza

class ChicagoPizzaStore(PizzaStore):
    def __init__(self):
        self.pizza = None

    def _create_pizza(self, pizza_type):
        ingredient_factory = ChicagoIngredientFactory()
        if pizza_type == "cheese":
            self.pizza = CheesePizza(ingredient_factory)
            self.pizza.set_name("Chicago Style Cheese Pizza")
        elif pizza_type == "pepperoni":
            self.pizza = PepperoniPizza(ingredient_factory)
            self.pizza.set_name("Chicago Pepperoni Pizza")
        elif pizza_type == "veggie":
            self.pizza = VeggiePizza(ingredient_factory)
            self.pizza.set_name("Chicago Veggie Pizza")
        return self.pizza
