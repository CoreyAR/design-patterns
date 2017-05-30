from Interfaces import DisplayMixIn, Observer

class TemperatureDisplay(Observer, DisplayMixIn):
    def __init__(self, subject):
        self.subject = subject
        self.subject.registerObserver(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.display("The temperature is {}.".format(self.temperature))

class HumidityDisplay(Observer, DisplayMixIn):
    def __init__(self, subject):
        self.subject = subject
        self.subject.registerObserver(self)

    def update(self, temperature, humidity, pressure):
        self.humidity = humidity
        self.display("Humidity is {}.".format(self.humidity))

class PressureDisplay(Observer, DisplayMixIn):
    def __init__(self, subject):
        self.subject = subject
        self.subject.registerObserver(self)

    def update(self, temperature, humidity, pressure):
        self.pressure = pressure
        self.display("The air pressure is {}.".format(self.pressure))
