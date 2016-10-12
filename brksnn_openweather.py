#!/usr/bin/env python3

import pyowm

API = input("Enter a valid API Key: ")
owm = pyowm.OWM(API)
#apicheck = owm.is_API_online()

#observation = owm.weather_at_place("Istanbul,TR")
observation = owm.weather_at_id(745044)

#CITY
city = observation.get_location()
cityname = city.get_name()
citylat = city.get_lat() #latitude
citylon = city.get_lon() #longitude
country = city.get_country()

#WEATHER
w = observation.get_weather()  
time = w.get_reference_time('iso')
sunset_time = w.get_sunset_time('iso')
sunrise_time = w.get_sunrise_time('iso')
wind = w.get_wind()
temperature = w.get_temperature('celsius')
humidity = w.get_humidity()
status = w.get_status()
weather_code = w.get_weather_code()

#print(apicheck)
#print(observation)
print("CITY: " + cityname)
print("COUNTRY: " + country)
print("Coord.: " + str(citylat) + ", " + str(citylon))
print("\nWEATHER DETAILS")
#print(w)
#print(type(w))
print("TIME: " + time)
print("SUNSET TIME: " + sunset_time)
print("SUNRISE TIME: " + sunrise_time)
print("WIND SPEED: " + str(wind['speed']) + " m/s")
print("WIND DIRECTION: " + str(wind['deg']) + "°")
print("TEMPERATURE: " + str(temperature['temp']) + "°C")
print("HUMIDITY: " + str(humidity) + "%")
print("STATUS: " + status)
#print(weather_code)
print("\n")
