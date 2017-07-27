
from Beverage import Beverage, Espresso
from Condiments import Soy, Mocha

# ------------------
# Java style decorator

espresso = Espresso()

soy_espresso = Soy(espresso)

print("Hi your, {} costs {}.".format(soy_espresso.getDescription(), soy_espresso.cost()))


# ---------------------
# Python style decorator

# @Mocha
# class Espresso(Beverage):
#     def __init__(self):
#         self.description = "Espresso"

#     def cost(self):
#         return 1.99

soy_espresso = Mocha(Espresso)
soy_mocha_espresso = Soy(soy_espresso())

print("Hi your, {} costs {}.".format(soy_mocha_espresso.getDescription(), soy_mocha_espresso.cost()))