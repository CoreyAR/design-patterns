from Interfaces import Subject

class WeatherData(Subject):
    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def registerObserver(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    def removeObserver(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notifyObservers(self,):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()
