from abc import ABCMeta, abstractmethod
from Beverage import Beverage

# ---------------------
# Java style decorator

class CondimentDecorator(Beverage):
    __metaclass__ = ABCMeta

    @abstractmethod
    def getDescription(self):
        pass


class Soy(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getDescription(self):
      return self.beverage.getDescription() + ", Soy"

    def cost(self):
      return .87 + self.beverage.cost()



# ---------------------
# Python style decorator

def Mocha(klass):
    class new_klass(klass):
      def __init__(self):
        self.beverage = klass() 

      def getDescription(self):
        return self.beverage.getDescription() + ", Mocha"

      def cost(self):
        return self.beverage.cost() + .99
    
    return new_klass