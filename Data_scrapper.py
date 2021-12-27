"""
===============================================================================
ENGR 13300 Fall 2021

Program Description
    This program calculates the 
    
Assignment Information
    Assignment:     Ind Project 
    Author:         Maximilian Drach, mdrach@purdue.edu 
                    
    Team ID:        LC5 - 07
    
Contributor:    Pranav, Shrishnkar pshrishankar@purdue.edu [repeat for each]
    My contributor(s) helped me:
    [ ] I am using Pranav's cordinates and adress code to get the cordinates for the historical data.
    this is code, that I did not write. It is here as a helper function.

ACADEMIC INTEGRITY STATEMENT
I have not used source code obtained from any other unauthorized
source, either modified or unmodified. Neither have I provided
access to my code to another. The project I am submitting
is my own original work.
===============================================================================
"""

import numpy as np
import requests
import json
from geopy.geocoders import Nominatim

def elevation(longitude, latitude):
    data = requests.get(f"https://api.open-elevation.com/api/v1/lookup?locations={longitude},{latitude}")
    file = data.json() #this a dictonary
    elevation = file['results'][0]['elevation']
    
    return elevation

# def floodTF(location): 
def hist_data(startDate, endDate, latitude, longitude):
    my_headers = {'Cache-Control': 'no-cache', 'api-key':'3ccbe94c35b4443ba14763606d2dd58e'}
    response = requests.get(f"https://api.oikolab.com/weather/?param=total_precipitation&param=temperature&param=dewpoint_temperature&param=relative_humidity&start={startDate}&end={endDate}&lat={latitude}&lon={longitude}&api-key=3ccbe94c35b4443ba14763606d2dd58e&resample_method=mean&freq=D&format=json", my_headers)
    
    return response.json()

geolocator = Nominatim(user_agent="Pranav Srisankar - Ind Project Engr 133")

def coords(address):
    try:
        location = geolocator.geocode(address)
    except:
        return "Error: Location does not exist."
    # Doesn't need to be precise since weather data is rather general over an area
    try:
        return [round(location.latitude,3), round(location.longitude, 3)]
    except:
        return "Error: Location does not exist."

def address(coords):
    try:
        location = geolocator.reverse(f"{coords[0]}, {coords[1]}")
    except:
        return "Error: Location does not exist."
    return location.address
