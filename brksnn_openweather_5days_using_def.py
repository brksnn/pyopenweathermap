#!/usr/bin/env python3

import pyowm

#API-KEY by buraksunan@yahoo.com.tr
#from http://openweathermap.org
owm = pyowm.OWM('7dc287b200e9a8bfe0d0c5fe61b01c87')
#apicheck = owm.is_API_online()

def Multi_Days_Forecasts(LOCATION, LIMIT):
    """Multi-Days Forecasts"""
    if isinstance(LOCATION, str) == True and LOCATION.isdigit() == False:
        fc = owm.daily_forecast(LOCATION,limit=LIMIT)
    elif LOCATION.isdigit() == True:
        LOCATION = int(LOCATION)
        fc = owm.daily_forecast_at_id(LOCATION,limit=LIMIT)
    else: 
        Warning('Try Again!!!')
    
    f = fc.get_forecast()
    time = f.get_reception_time('iso')
    return (f,time)
    
#CITY
def Location_Data(f):
    city = f.get_location()
    cityname = city.get_name()
    citylat = city.get_lat() #latitude
    citylon = city.get_lon() #longitude
    country = city.get_country()
    return (cityname,citylat,citylon,country)

#WEATHER
def Weather_Data(f, LIMIT):
    w = f.get_weathers()
    wind=[]; snow=[]; rain=[]; clouds=[]; temperature=[]; humidity=[]; status=[]; 
    for i in range(0,LIMIT):
        wind.append(w[i].get_wind())
        snow.append(w[i].get_snow())
        rain.append(w[i].get_rain())
        clouds.append(w[i].get_clouds())
        temperature.append(w[i].get_temperature('celsius'))
        humidity.append(w[i].get_humidity())
        status.append(w[i].get_status())
    return (wind,snow,rain,clouds,temperature,humidity,status)

def PRINT_DATA(LOC, WEA, LIMIT, TIME):
    #CITY DETAILS
    print("CITY: " + LOC[0])
    print("COUNTRY: " + LOC[3])
    print("Coord.: " + str(LOC[1]) + ", " + str(LOC[2]))
    print("CURRENT TIME: " + TIME + "\n")
    #WEATHER DETAILS
    for i in range(0,LIMIT):
        print("WEATHER DETAILS: " + "GUN_" + str(i+1))
        print("WIND SPEED: " + str(WEA[0][i]['speed']) + " m/s")
        if 'deg' in WEA[0]:
            print("WIND DIRECTION: " + str(WEA[0][i]['deg']) + "°")
        else:
            pass
        print("SNOW: " + str(WEA[1][i]) + " mm")	
        if 'all' in WEA[2]:
            print("RAIN: " + str(WEA[2][i]['all']) + " mm")
        else:
            print("RAIN: " + str(0) + " mm")
        print("CLOUDS: " + str(WEA[3][i]) + "%")
        print("TEMPERATURE: " + str(WEA[4][i]['day']) + "°C")
        print("HUMIDITY: " + str(WEA[5][i]) + "%")
        print("STATUS: " + WEA[6][i])
        print("\n")

#INPUT
def INPUT():
    f = input("Enter the location name (e.g.'Istanbul,TR') or location id: ")
    limit = input("How many days do you want?  ")
    return (f,int(limit))

F = INPUT() #call the INPUT function
FORE = Multi_Days_Forecasts(F[0], F[1])
LOC = Location_Data(FORE[0])
WEA = Weather_Data(FORE[0], F[1])
P = PRINT_DATA(LOC, WEA, F[1], FORE[1])