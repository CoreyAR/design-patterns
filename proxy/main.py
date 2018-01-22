import sys
sys.path.append('../')

from state.gumball import GumballMachine


class GumballProMachine(GumballMachine):
    def __init__(self, count, location):
        super(GumballProMachine, self).__init__(count)
        self.location = location
    
    def get_location(self):
        return self.location

class GumballProxyMonitor(object):
    def __init__(self, machine):
        self.machine = machine
    
    def report(self):
        print('Gumball Machine: {}\nCurrent Inventory: {}\nCurrent State: {}\n '.format(self.machine.get_location(), self.machine.get_count(), self.machine.get_state()))

    def refill(self, technician_location):
        # This proxy arbitrarily controls access to increasing the gumball count based on location of the machine and technician
        if self.machine.location == technician_location:
            self.machine.count += 100


if __name__ == '__main__':
    gumball_machine = GumballProMachine(5, 'Nashville')
    monitor = GumballProxyMonitor(gumball_machine)
    gumball_machine.insert_quarter()
    monitor.report()