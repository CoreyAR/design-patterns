from os import path
import types

# https://github.com/jdorfman/awesome-json-datasets#cars
ford_list = [
    {"model_name":"Aerostar","model_make_id":"ford"},
    {"model_name":"Anglia","model_make_id":"ford"},
    {"model_name":"Artic","model_make_id":"ford"},
    {"model_name":"Aspire","model_make_id":"ford"},
    {"model_name":"Bantam","model_make_id":"ford"},
    {"model_name":"Bronco","model_make_id":"ford"},
    {"model_name":"Bronco II","model_make_id":"ford"}
]

gmc_dict = {
    "Acadia": {"model_make_id":"gmc"},
    "Autonomy": {"model_make_id":"gmc"},
    "Canyon": {"model_make_id":"gmc"},
    "Envoy": {"model_make_id":"gmc"},
    "EV1": {"model_make_id":"gmc"},
    "Firebird": {"model_make_id":"gmc"},
    "Jimmy": {"model_make_id":"gmc"},
    "Safari": {"model_make_id":"gmc"},
    "Savana": {"model_make_id":"gmc"},
    "Sierra": {"model_make_id":"gmc"}
}


def acura_generator():
    with open(path.join(path.dirname(path.realpath(__file__)),'acura.csv')) as f:
        for line in f:
            line = line.rstrip("\n").split(",", 1)
            yield {"model_name":line[0],"model_make_id": line[1]}

cadillac_tuple = (
    {"model_name":"60","model_make_id":"cadillac"},
    {"model_name":"61","model_make_id":"cadillac"},
    {"model_name":"62","model_make_id":"cadillac"},
    {"model_name":"6239D","model_make_id":"cadillac"},
    {"model_name":"Allante","model_make_id":"cadillac"},
    {"model_name":"ATS","model_make_id":"cadillac"},
    {"model_name":"ATS Coupe","model_make_id":"Cadillac"},
    {"model_name":"Aurora","model_make_id":"cadillac"}
)

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