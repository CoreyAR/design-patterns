# Facade Enample

class HomeExpenses:
    def __init__(self, n=0): 
        self.total = n
    
    def add(self, n):
        self.total += n

class WorkExpenses:
    def __init__(self, n=0): 
        self.total = n
    
    def add(self, n):
        self.total += n

class HobbyExpenses:
    def __init__(self, n=0): 
        self.total = n
    
    def add(self, n):
        self.total += n


class Facade:
    def calcHomeExp(self, n):
        if hasattr(self, 'hm'):
            self.hm.add(n)
        else:
            self.hm = HomeExpenses(n)
        return self.hm.total

    def calcWorkExp(self, n):
        if hasattr(self, 'wrk'):
            self.wrk.add(n)
        else: 
            self.wrk = WorkExpenses(n)
        return self.wrk.total

    def calcHobbyExp(self,n):
        if hasattr(self, 'hby'):
            self.hby.add(n)
        else: 
            self.hby = HobbyExpenses(n)
        return self.hby.total
    
    def print_total(self):
        total = self.hm.total if hasattr(self, 'hm') else 0
        total += self.wrk.total if hasattr(self, 'wrk') else 0
        total += self.hby.total if hasattr(self, 'hby') else 0
        print('Total expenses from Facade are {}'.format(total))


# Using static methods we can futher simplify the interface of the Facade by not requiring the user to instiate the class

class StaticFacade:
    hm = 0
    wrk = 0
    hby = 0

    def calcHomeExp(n):
        StaticFacade.hm += n

    calcHomeExp = staticmethod(calcHomeExp)

    def calcWorkExp(n):
        StaticFacade.wrk += n

    calcWorkExp = staticmethod(calcWorkExp)

    def calcHobbyExp(n):
        StaticFacade.hby += n

    calcHobbyExp = staticmethod(calcHobbyExp)
    
    def print_total():
        total = StaticFacade.hm
        total += StaticFacade.wrk
        total += StaticFacade.hby
        print('Total expenses from StaticFacade are {}'.format(total))
    
    print_total = staticmethod(print_total)

if __name__ == "__main__":
    facade = Facade()
    facade.calcHomeExp(3)
    home = facade.calcHomeExp(3)
    work = facade.calcWorkExp(4)
    hobby = facade.calcHobbyExp(5)
    facade.print_total()

    work = StaticFacade.calcWorkExp(4)
    hobby = StaticFacade.calcHobbyExp(5)
    StaticFacade.print_total()
