# Composite

class Dealership(object):
    def add(self, component):
        raise NotImplementedError
    
    def remove(self, component):
        raise NotImplementedError
    
    def get_child(self):
        raise NotImplementedError
    
    def get_name(self):
        raise NotImplementedError

    def get_description(self):
        raise NotImplementedError

    def get_price(self):
        raise NotImplementedError
    
    def print(self):
        raise NotImplementedError

    def get_child(self, idx):
        raise NotImplementedError


class Make(CarComponent):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.makes = {}

    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description

    def print(self):
        print('{} - {}'.format(self.name, self.description))
        for key in self.makes.keys():
            for car in self.makes[key]:
                car.print()

    def add(self, car_list):
        self.makes[car_list[0]['model_make_id']] = car_list
    
    def remove(self, make):
        del d[make]    
    
    def get_child(self, idx):
        return self.makes[idx]




class Model(CarComponent):
    def __init__(self, car):
        self.car

    def get_name(self):
       return  self.car.model_make_id
    
    def get_description(self):
        return self.car.model_name

    def print(self):
        print('{} is made by {}.'.format(self.car['model_name'], self.car['model_make_id']))

# Composite Iterator
