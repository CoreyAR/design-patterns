from abc import ABCMeta, abstractmethod

class Beverage(object):
    __metaclass__ = ABCMeta

    def __init__(self, description="Unknown Beverage"):
        self.description = description
    
    def getDescription(self):
        return self.description
    
    @abstractmethod
    def cost(self):
        pass


class Espresso (Beverage):
  def __init__(self):
    self.description = "Espresso"

  def cost(self):
    return 1.99
