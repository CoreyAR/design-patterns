import types
from car_data import ford_list, gmc_dict, cadillac_tuple, acura_generator

# https://github.com/jdorfman/awesome-json-datasets#cars




# Function to get make and model
def print_make_model(car):
    print('{} is made by {}.'.format(car['model_name'], car['model_make_id']))


class CustomIterator(object):
    def __init__(self, cars):
        self.cars = cars
        self.idx = 0
        if isinstance(self.cars, dict):
            self.keys = self.cars.keys()
            self.length = len(self.keys)
        elif not isinstance(self.cars, types.GeneratorType):
            self.length = len(self.cars)

    def __iter__(self):
        return self

    def next(self):
        if isinstance(self.cars, types.GeneratorType):
            return next(self.cars.__iter__()) 
        elif self.length > self.idx:
            if isinstance(self.cars, dict):
                k = next(self.keys.__iter__())
                car = self.cars[k]
                car['model_name'] = k
                self.idx += 1
                return car
            car = self.cars[self.idx]
            self.idx += 1
            return car
        else:
            raise StopIteration

    def back(self):
        if self.idx <= 0:
            raise StopIteration

        if isinstance(self.cars, types.GeneratorType):
            raise NotImplementedError
        elif self.length > self.idx:
            if isinstance(self.cars, dict):
                self.idx -= 1
                k = self.keys[idx]
                car = self.cars[k]
                car['model_name'] = k
                return car
            self.idx -= 1
            car = self.cars[self.idx]
            return car
        else:
            raise StopIteration
    

    def has_next(self):
        if self.idx < self.length:
            return True
        return False


if __name__ == '__main__':
    ford_cars = CustomIterator(ford_list)
    gmc_cars = CustomIterator(gmc_dict)
    acura_cars = CustomIterator(acura_generator())
    cadillac_cars = CustomIterator(cadillac_tuple)

    for c in ford_cars:
        print_make_model(c)
    
    for c in CustomIterator(gmc_dict):
        print_make_model(c)

    for c in acura_cars:
        print_make_model(c)
    
    for c in cadillac_cars:
        print_make_model(c)

    ford_cars_2 = CustomIterator(ford_list)
    c = ford_cars_2.next()
    print_make_model(c)
    c = ford_cars_2.next()
    print_make_model(c)
    c = ford_cars_2.back()
    print_make_model(c)
    c = ford_cars_2.back()
    print_make_model(c)
    c = ford_cars_2.back()
    print_make_model(c)