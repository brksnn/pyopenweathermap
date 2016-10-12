#!/usr/bin/env python3

import pyowm

API = input("Enter a valid API Key: ")
owm = pyowm.OWM(API)
#apicheck = owm.is_API_online()

#Multi-Days Forecasts
LIMIT = 5
fc = owm.daily_forecast_at_id(745044,limit=LIMIT)
f = fc.get_forecast()
time = f.get_reception_time('iso')

#CITY
city = f.get_location()
cityname = city.get_name()
citylat = city.get_lat() #latitude
citylon = city.get_lon() #longitude
country = city.get_country()

sunset_time=[]
sunrise_time=[]
wind=[]
snow=[]
rain=[]
clouds=[]
temperature=[]
humidity=[]
status=[]
weather_code=[]

#WEATHER
w = f.get_weathers()
for i in range(0,LIMIT):
	#sunset_time.append(w[i].get_sunset_time('iso'))
	#sunrise_time.append(w[i].get_sunrise_time('iso'))
	wind.append(w[i].get_wind())
	snow.append(w[i].get_snow())
	rain.append(w[i].get_rain())
	clouds.append(w[i].get_clouds())
	temperature.append(w[i].get_temperature('celsius'))
	humidity.append(w[i].get_humidity())
	status.append(w[i].get_status())
	weather_code.append(w[i].get_weather_code())


#print(apicheck)
print("CITY: " + cityname)
print("COUNTRY: " + country)
print("Coord.: " + str(citylat) + ", " + str(citylon))
print("CURRENT TIME: " + time + "\n")
for i in range(0,LIMIT):
	print("WEATHER DETAILS: " + "GUN_" + str(i+1))
	#print("SUNSET TIME: " + sunset_time[i])
	#print("SUNRISE TIME: " + sunrise_time[i])
	print("WIND SPEED: " + str(wind[i]['speed']) + " m/s")
	if 'deg' in wind:
		print("WIND DIRECTION: " + str(wind[i]['deg']) + "°")
	else:
		pass
	print("SNOW: " + str(snow[i]) + " mm")	
	if 'all' in rain:
		print("RAIN: " + str(rain[i]['all']) + " mm")
	else:
		print("RAIN: " + str(0) + " mm")
	print("CLOUDS: " + str(clouds[i]) + "%")
	print("TEMPERATURE: " + str(temperature[i]['day']) + "°C")
	print("HUMIDITY: " + str(humidity[i]) + "%")
	print("STATUS: " + status[i])
	print("\n")

