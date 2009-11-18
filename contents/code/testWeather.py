#!/usr/bin/env python
 
from weatherInfo import WeatherInfo
from weather import Weather
 
wi = WeatherInfo()
wi.parse("Munich,Germany")
 
weather = Weather()
weather.extractData(wi,"SI")
weather.show()
