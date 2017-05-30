from WeatherData import WeatherData
from Displays import TemperatureDisplay, PressureDisplay, HumidityDisplay


class WeatherStation(object):
    def __init__(self):
        self.weather_data = WeatherData()
        self.temperature_display = TemperatureDisplay(self.weather_data)
        self.pressure_display = PressureDisplay(self.weather_data)
        self.humidity_display = HumidityDisplay(self.weather_data)
        # Simulate weather measurements
        self.weather_data.setMeasurements(80, 20, 30)
        self.weather_data.setMeasurements(40, 30, 35)
        self.weather_data.setMeasurements(90, 50, 75)


WeatherStation()
