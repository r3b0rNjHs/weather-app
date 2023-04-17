class Forecast:
    def __init__(self, today, tomorrow):
        self.today = today
        self.tomorrow = tomorrow

    def to_dict(self):
        return {
            'today': self.today.to_dict(),
            'tomorrow': self.today.to_dict(),
        }


class ForecastDetails:
    def __init__(self, temperature, humidity, precipitation):
        self.temperature = temperature
        self.humidity = humidity
        self.precipitation = precipitation

    def to_dict(self):
        return {
            'temperature': self.temperature,
            'humidity': self.humidity,
            'precipitation': self.precipitation
        }
