# Automated driving adaptor for automatic and manual cars

class Car(object):
    """Base Car class"""
    def __init__(self):
        self.gear = 'P'
        self.speed = 0
        self.gas = False
        self.brake = True

    def accelerate(self):
        print('Gas pressed.')
        while(self.gas):
            self.speed += 1

    def deccelerate(self):
        print('Brake pressed.')
        self.gas = False
        self.speed = int(self.speed - 1)


class Automatic(Car):
    """Automatic car class"""
    def __init__(self):
        Car.__init__(self)
        self.gears = ['P', 'N', 'D', 'L']

    def low_gear(self):
        self.gear = 'L'


class Manual(Car):
    """Manual car class that we want to act like an automatic car"""
    def __init__(self):
        Car.__init__(self)
        self.gears = ['P', 'N', 1, 2, 3, 4, 5]

    def shift_up(self):
        curr_idx = self.gears.index(self.gear)
        self.gear = self.gears[curr_idx + 1]
        print('Shifted up to {}.'.format(self.gear))
    
    def shift_down(self):
        curr_idx = self.gears.index(self.gear)
        self.gear = self.gears[curr_idx - 1]
        print('Shifted down to {}.'.format(self.gear))


class CarAdapter(object):
    """Adapter class to make an manual car act like an automatic car"""
    def __init__(self, manual):
        self._manual = manual
    
    def low_gear(self):
        if type(self.gear) is int and self.gear > 1:
            while(self.gear != 1):
                self._manual.shift_down
    
    def accelerate(self):
        self._manual.accelerate()
        self._manual.shift_up()

    def deccelerate(self):
        self._manual.deccelerate()
        self._manual.shift_down()


class Drive(object):
    """Class to control the car"""
    def __init__(self, car_object):
        self.car = car_object
    
    def accelerate(self):
        self.car.accelerate()
    
    def deccelerate(self):
        self.car.deccelerate()


def main():
    # Plug in
    manual = Manual()
    autonomous_car = CarAdapter(manual)
    driverless_car = Drive(autonomous_car)

    driverless_car.accelerate()
    driverless_car.deccelerate()

if __name__ == "__main__":
    main()