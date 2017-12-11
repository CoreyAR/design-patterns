from abc import ABCMeta, abstractmethod
class GumballState(object):
    __metaclass__ = ABCMeta

    def __init__(self, machine):
        self.machine = machine

    @abstractmethod
    def insert_quarter(self):
        pass

    @abstractmethod
    def eject_quarter(self):
        pass

    @abstractmethod
    def turn_crank(self):
        pass

    @abstractmethod
    def dispense():
        pass

class SoldState(GumballState):
    def insert_quarter(self):
        print('Please wait, we\'re dispensing a gumball.')

    def eject_quarter(self):
        print('Sorry you already turned the crank.')

    def turn_crank(self):
        print('Can\'t turn the crank twice.')

    def dispense(self):
        print('A gumball comes rolling out the slot.')
        self.machine.count = self.machine.count - 1
        if (self.machine.count != 0):    
            self.machine.state = self.machine.NO_QUARTER
        else:
            self.machine.state = self.machine.SOLD_OUT

class SoldOutState(GumballState):
    def insert_quarter(self):
       print('You can\'t insert a quarter. The machine is sold out.')

    def eject_quarter(self):
       print('You can\'t eject, you haven\'t inserted a quarter yet.')

    def turn_crank(self):
        print('You turned but there are no gumballs.')

    def dispense(self):
        print('No gumball dispensed.')

class NoQuarterState(GumballState):
    def insert_quarter(self):
        print('You inserted a quarter.')
        self.machine.state = self.machine.HAS_QUARTER

    def eject_quarter(self):
        print('You have\'nt inserted a quarter.')

    def turn_crank(self):
        print('You turned but there is no quarter.')

    def dispense(self):
        print('You need to pay first.')

class HasQuarterState(GumballState):
    def insert_quarter(self):
        print('You can\'t insert another quarter.')

    def eject_quarter(self):
        self.machine.state = self.machine.NO_QUARTER
        print('Quarter returned')

    def turn_crank(self):
        print('You turned ...')
        self.machine.state = self.machine.SOLD

    def dispense(self):
        print('No gumball dispensed. Turn crank.')


class GumballMachine(object):
    def __init__(self, count):
        self.SOLD_OUT = SoldOutState(self)
        self.NO_QUARTER = NoQuarterState(self)
        self.HAS_QUARTER = HasQuarterState(self)
        self.SOLD = SoldState(self)

        self.state = self.SOLD_OUT
        self.count = count
        if self.count > 0:
            self.state = self.NO_QUARTER
    
    def insert_quarter(self):
        self.state.insert_quarter()
    
    def eject_quarter(self):
        self.state.eject_quarter()

    def turn_crank(self):
        self.state.turn_crank()
        self.state.dispense()
    
    def setState(self, state):
        self.state = state
           

if __name__ == '__main__':
    gumball_machine = GumballMachine(5)
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()