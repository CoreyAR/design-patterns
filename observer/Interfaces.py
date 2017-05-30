from abc import ABCMeta, abstractmethod

class Observer(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, *args, **kwargs):
        pass

class DisplayMixIn(object):
    __metaclass__ = ABCMeta

    def display(self, condition):
        print("Current: {}".format(condition))

class Subject(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def registerObserver(self):
        pass

    @abstractmethod
    def removeObserver(self):
        pass

    @abstractmethod
    def notifyObservers(self):
        pass
