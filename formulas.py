"""
===============================================================================
ENGR 13300 Fall 2021

Program Description
    This formates the weather api's json to a list and it has specilized weather functions
    
Assignment Information
    Assignment:     Ind Project 
    Author:         Maximilian Drach, mdrach@purdue.edu 
                    
    Team ID:        LC5 - 07
    
Contributor:    Name, login@purdue [repeat for each]
    My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.

ACADEMIC INTEGRITY STATEMENT
I have not used source code obtained from any other unauthorized
source, either modified or unmodified. Neither have I provided
access to my code to another. The project I am submitting
is my own original work.
===============================================================================
"""

import Data_scrapper as dasc
import matplotlib.pyplot as plt
import numpy as np
import math as m
import ast

def evap_rate(Temp, altitude, humidity, latitude, hist_Tdew=0):

    if (isinstance(Temp, (float, int))==True) and (isinstance(altitude,(float, int))==True) and (isinstance(humidity,(float, int)) ==True) and (isinstance(humidity,(float, int))==True) and (isinstance(latitude,(float, int))==True) and (isinstance(hist_Tdew,(float, int))==True):
        #Temp (C)
        #altitude (m)
        #humidity (0-100)
        
        gi = 243.12 #conversion constant
        B = 17.62 #constant
        if hist_Tdew !=0:
            #http://irtfweb.ifa.hawaii.edu/~tcs3/tcs3/Misc/Dewpoint_Calculation_Humidity_Sensor_E.pdf
            td1 = gi*(m.log(humidity/100)+((B*Temp)/(gi+Temp)))
            td2 = B-(m.log(humidity/100)+((B*Temp)/(gi+Temp)))
            Tdew = td1/td2 #dew tempiture
            
        else:
            Tdew = hist_Tdew
        
        Tm = Temp + .0006*altitude#temp ajustest for altitude
        
        e1 = (700*Tm/(100-latitude)) + (15*(Temp-Tdew))
        e2 = 80 - Temp
        Evaporation_rate = e1/e2 #mm/day
        #https://www.sciencedirect.com/science/article/pii/0002157177900073
        return Evaporation_rate
    else:
        return "Please enter a int or float for all the values!!!"

def historical_datasets():

    
    location = ['Wilkes-Barre, PA', 'Florida Keys, FL', 'Denham Springs, LA', 'Rapid City, SD', 'Bloomington, IN', 'Denver, CO', 'Helena, Montana', "New York City, NY", "Annapolis, MD", "Seattle, WA", "Seattle, WA", "Seattle, WA","Seattle, WA", "Seattle, WA", 'Helena, Montana', "Denver, CO", 'Helena, Montana', "Denver, CO"]
    flood_start = ["2011-09-02", "2017-09-02", "2016-08-08", "1972-06-07", "2008-06-05", "2021-06-01","2018-07-01","2011-05-01", "2008-11-01", "2001-11-01", "1998-12-01","1999-12-01","2016-12-01", "2017-08-01", "2017-08-01", "1982-07-01", "1974-07-01"]
    
    #flood t/f
    flood_tf = [[0,0,0,0,0,0,1,1,1,1,1],[0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0],[0,0,0,0,0,1,1,1,1,1,1,1,1],[0,0,1,1,1,1],[0,0,0,1,1,1,1,1,1,1,1,1,1],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    flood_end = ["2011-09-12", "2017-09-18", "2016-08-20", "1972-06-12", "2008-06-17", "2021-06-30", "2018-07-31","2011-05-31","2008-11-30","2001-11-30", "1998-12-31","1999-12-31","2016-12-31", "2017-08-31", "2017-08-31","1982-07-31", "1974-07-31"]

    #historical_data_names=['day case number', 'location', 'longitude', 'latitude', 'elevation','rainfall(mm)','temp(C)','dewpoint temp(C)','humdity(0-1)', 'evap rate', 'flood happend (0 or 1)']
    #data = pd.DataFrame(columns=historical_data_names)

    historical_data = []
    historical_data_pts = []
    for i in range(len(flood_start)):
        n=0
        la, lo = dasc.coords(location[i])
        #lat.append(la)
        #long.append(lo)

        data = dasc.hist_data(flood_start[i],flood_end[i],la,lo)
        data = data['data']
        #needed to strip the strings off the data
        data = data.rstrip("'")
        data = data.lstrip("'")
        #coverts string to dict
        data = ast.literal_eval(data)


        cumulative_rainfall = 0

        for j in range(len(data['data'])):
            elevation = data['data'][j][2]
            rainfall = data['data'][j][4]*24
            temp = data['data'][j][5]
            dewTemp = data['data'][j][6]
            humidity = data['data'][j][7]
            evap = evap_rate(temp, elevation, humidity, la, dewTemp)


            cumulative_rainfall = cumulative_rainfall+rainfall-evap
            if cumulative_rainfall < 0:
                cumulative_rainfall = 0

            #historical_data_names=['day case number', 'location', 'longitude', 'latitude', 'elevation','rainfall(mm)','temp(C)','dewpoint temp(C)','humdity(0-1)', 'evap rate', 'flood happend (0 or 1)']
            x=[n, location[i], lo, la, elevation, rainfall, temp, dewTemp, humidity, evap, flood_tf[i][j]]
            y=[cumulative_rainfall, elevation, flood_tf[i][j]]

            historical_data.append(x)
            historical_data_pts.append(y)
            n = n+1


    return historical_data_pts, historical_data


def cumulative_rainfall(past_rainfall, temp, altitude, humidity, latitude):

    if (isinstance(past_rainfall, list) == True) and (isinstance(temp, list)==True) and (isinstance(humidity, list)==True) and (isinstance(altitude,(float, int)) == True) and (isinstance(latitude,(float, int)) == True):
    #either enter temp, humidit, rainfall as a list 
    #altitude and latitude must a be a scalar
        rainfall = 0
        
        for i in range(len(past_rainfall)):
            evaporation = evap_rate(temp[i], altitude, humidity[i], latitude)
            rainfall = rainfall + past_rainfall[i] - evaporation
    
        if rainfall >= 0:
            return rainfall
        else:
            return 0
    else:
        return "past_rainfall, temp, and humidity must be list. \naltitude and latitude must be int or float"


def prediction_formula(data_list=0):

    #this one makes it so you dont have to re-load in the past data from the API or you have your own list gathered from hisorical data
    #this assumes you already have your previous data, if not run the prediction function
    #def make sure the rain fall is from the past 10 day
    #gets the data from the historical dataset
    if (data_list, list):
         hist_dp = data_list
    else:
        hist_dp, hist_d = historical_datasets()


    #turns the data to a numpy array
    hist_dp_np = np.asarray(hist_dp)

    #cumulative rainfall
    rain = hist_dp_np[:,0]
    #elevation
    elevation = hist_dp_np[:,1]
    #flood t/f
    tf = hist_dp_np[:,2]

    #this create an stacked array to create the Coefficint matrix
    A=np.vstack([rain, elevation, np.ones(len(rain))]).T

    #using linear alegebra properties of method of least squares, we get the linear flood approximation
    # begin by clarifying exactly what we will mean by a “best approximate solution” to an inconsistent matrix equation Ax=v
    m1, m2, d = np.linalg.lstsq(A, tf, rcond=None)[0]
    
    
    #m1 is slope for cumulative rainfall, m2 is the slope for elevation, and d is the z-axis
    #z = (m1*cumulative_rainfall)+(m2*altitude)+d

    return m1, m2, d

def prediction_eff_z(cumulative_rainfall, altitude, m1, m2, d):
    #this just retunrs the z probility given the m1, m2, d and the rainfall and altititude
    z = (m1*cumulative_rainfall)+(m2*altitude)+d

    return z
