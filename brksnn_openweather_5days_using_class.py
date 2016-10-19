#!/usr/bin/env python3

import pyowm

class PyOpenWeatherMap():
    def __init__(self):
        self.API = input("Enter a valid API Key: ")
        self.owm = pyowm.OWM(self.API)
        self.loc = input("Enter the location name (e.g.'Istanbul,TR') or location id: ")
        self.limit = input("How many days do you want?  ")
        self.limit = int(self.limit)
        self.PRINT_DATA()
    
    def Multi_Days_Forecasts(self):
        """Multi-Days Forecasts"""
        if isinstance(self.loc, str) == True and self.loc.isdigit() == False:
            self.fc = self.owm.daily_forecast(self.loc,self.limit)
        elif self.loc.isdigit() == True:
            self.loc = int(self.loc)
            self.fc = self.owm.daily_forecast_at_id(self.loc,self.limit)
        else: 
            Warning('Try Again!!!')
        
        self.f = self.fc.get_forecast()
        self.time = self.f.get_reception_time('iso')
        return (self.f,self.time)
        
    #CITY
    def Location_Data(self):
        self.city = self.f.get_location()
        self.cityname = self.city.get_name()
        self.citylat = self.city.get_lat() #latitude
        self.citylon = self.city.get_lon() #longitude
        self.country = self.city.get_country()
        return (self.cityname,self.citylat,self.citylon,self.country)
    
    #WEATHER
    def Weather_Data(self):
        self.w = self.f.get_weathers()
        self.wind=[]; self.snow=[]; self.rain=[];self.clouds=[];
        self.temperature=[]; self.humidity=[]; self.status=[]; 
        for i in range(0,self.limit):
            self.wind.append(self.w[i].get_wind())
            self.snow.append(self.w[i].get_snow())
            self.rain.append(self.w[i].get_rain())
            self.clouds.append(self.w[i].get_clouds())
            self.temperature.append(self.w[i].get_temperature('celsius'))
            self.humidity.append(self.w[i].get_humidity())
            self.status.append(self.w[i].get_status())
        return (self.wind,self.snow,self.rain,self.clouds,\
                self.temperature,self.humidity,self.status)
    
    def PRINT_DATA(self):
        self.Multi_Days_Forecasts()
        self.Location_Data()
        self.Weather_Data()
        #CITY DETAILS
        print("CITY: " + self.cityname)
        print("COUNTRY: " + self.country)
        print("Coord.: " + str(self.citylat) + ", " + str(self.citylon))
        print("CURRENT TIME: " + self.time + "\n")
        #WEATHER DETAILS
        for i in range(0,self.limit):
            print("WEATHER DETAILS: " + "DAY_" + str(i+1))
            print("WIND SPEED: " + str(self.wind[i]['speed']) + " m/s")
            print("SNOW: " + str(self.snow[i]) + " mm")	
            if 'all' in self.rain:
                print("RAIN: " + str(self.rain[i]['all']) + " mm")
            else:
                print("RAIN: " + str(0) + " mm")
            print("CLOUDS: " + str(self.clouds[i]) + "%")
            print("TEMPERATURE: " + str(self.temperature[i]['day']) + "°C")
            print("HUMIDITY: " + str(self.humidity[i]) + "%")
            print("STATUS: " + self.status[i])
            print("\n")

F = PyOpenWeatherMap()