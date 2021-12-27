"""
===============================================================================
ENGR 13300 Fall 2021

Program Description
    This program allows people to demo the probablity models

    prediction_formatted_eff, formates the prediction to the terminal
    in a clear way, that show both the x,y slopes and the z-axis. It also returns outputs of the probality function

    demo_flood_prob_location, this function allows the user to test out the flood probility givent the cumulative rainfall and the elevation/altitude.
    this functions uses the prediction_formatted_eff to allow a the user to see the inner workings of the function

    demo_cumulative_rainfall(), this function allows the users to demo the cumulitave rainfall function

    demo_flood_prob_values(), this list a ton probability values given diffent cumulative rainfall and elevation inputs

    
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
import formulas as f
import datetime
import ast
def prediction_formatted_eff(cumulative_rainfall, altitude, m1, m2, d):
    #outputs a formatted answer of the flood probility given the x,y slopes and z-axis
    print("cumlative rainfall slope (m1) = ", m1)
    print("elevation slope (m2) = ", m2)
    print("z-axis (d) = ", d)

    print("\n")

    print("probability of flood (z) = m1*cumulative_rainfall + m2*altitude + d")
    print("probability of flood (z) = ", m1,"*",cumulative_rainfall, " + ", m2, "*", altitude, " + ", d)
    #add up the slopes to get the z values which will be from 0-1
    z = (m1*cumulative_rainfall)+(m2*altitude)+d
    print("probability of flood (z) = ", z, "    or    ", z*100, "%")

    return z

def demo_flood_prob_location(cumulative_rainfall, altitude):
    data_list, teresa = f.historical_datasets()
    m1, m2, d = f.prediction_formula(data_list)

    z = prediction_formatted_eff(cumulative_rainfall,altitude,m1,m2,d)
    return z, m1, m2, d


def demo_cumulative_rainfall():
    rainfall_10_days_mm = [20,31,22,23,24,25,26,27,18,19]
    temp = [60,61,62,63,64,65,66,67,68,69], 
    humidity = [.60,.61,.62,.63,.64,.65,.66,.67,.68,.69]

    location = "Purdue University"
    la, lo = dasc.coords(location)
    alt = dasc.elevation(lo, la)


    print("rainfall from past 10 days mm pre-set demo values\n", rainfall_10_days_mm)
    print("tempetures pre-set demo values\n", temp)
    print("humidity pre-set demo values\n", humidity)

    print('\npre-set demo location: ', location)
    print('(latitude,longitude): ', la,lo)

    
    cumulative_rain = f.cumulative_rainfall(rainfall_10_days_mm, temp, alt, humidity, la)
    print('demo cumulative rainfall value: ', cumulative_rain, '(mm)')
    return cumulative_rain

def demo_flood_prob_values():

    #oupts the probablity of flood, with different elevations and cumulative ranifalls
    data_list, useless = f.historical_datasets()
    m1, m2, d = f.prediction_formula(data_list)

    print("\n\n\n\n")
    print(f.prediction_eff_z(10,1000,m1,m2,d))
    print(f.prediction_eff_z(10,500,m1,m2,d))
    print(f.prediction_eff_z(10,300,m1,m2,d))
    print(f.prediction_eff_z(10,200,m1,m2,d))
    print(f.prediction_eff_z(10,100,m1,m2,d))
    print(f.prediction_eff_z(10,100,m1,m2,d))
    print(f.prediction_eff_z(10, 10,m1,m2,d))
    print(f.prediction_eff_z(10, 5,m1,m2,d))
    print(f.prediction_eff_z(10, 0,m1,m2,d))
    print(f.prediction_eff_z(10, -10,m1,m2,d))
    print("\n\n\n")
    print(f.prediction_eff_z(7.5,1000,m1,m2,d))
    print(f.prediction_eff_z(7.5,500,m1,m2,d))
    print(f.prediction_eff_z(7.5,300,m1,m2,d))
    print(f.prediction_eff_z(7.5,200,m1,m2,d))
    print(f.prediction_eff_z(7.5,100,m1,m2,d))
    print(f.prediction_eff_z(7.5,50,m1,m2,d))
    print(f.prediction_eff_z(7.5, 10,m1,m2,d))
    print(f.prediction_eff_z(7.5, 5,m1,m2,d))
    print(f.prediction_eff_z(7.5, 0,m1,m2,d))
    print(f.prediction_eff_z(7.5, -10,m1,m2,d))
    print("\n\n\n")
    print(f.prediction_eff_z(5,1000,m1,m2,d))
    print(f.prediction_eff_z(5,500,m1,m2,d))
    print(f.prediction_eff_z(5,300,m1,m2,d))
    print(f.prediction_eff_z(5,200,m1,m2,d))
    print(f.prediction_eff_z(5,100,m1,m2,d))
    print(f.prediction_eff_z(5,50,m1,m2,d))
    print(f.prediction_eff_z(5, 10,m1,m2,d))
    print(f.prediction_eff_z(5, 5,m1,m2,d))
    print(f.prediction_eff_z(5, 0,m1,m2,d))
    print(f.prediction_eff_z(5, -10,m1,m2,d))

    print("\n\n\n")
    print(f.prediction_eff_z(5,1000,m1,m2,d))
    print(f.prediction_eff_z(5,500,m1,m2,d))
    print(f.prediction_eff_z(5,300,m1,m2,d))
    print(f.prediction_eff_z(5,200,m1,m2,d))
    print(f.prediction_eff_z(5,100,m1,m2,d))
    print(f.prediction_eff_z(5,50,m1,m2,d))
    print(f.prediction_eff_z(5, 10,m1,m2,d))
    print(f.prediction_eff_z(5, 5,m1,m2,d))
    print(f.prediction_eff_z(5, 0,m1,m2,d))
    print(f.prediction_eff_z(5, -10,m1,m2,d))

    print("\n\n\n")

    print(f.prediction_eff_z(1,1000,m1,m2,d))
    print(f.prediction_eff_z(1,500,m1,m2,d))
    print(f.prediction_eff_z(1,300,m1,m2,d))
    print(f.prediction_eff_z(1,200,m1,m2,d))
    print(f.prediction_eff_z(1,100,m1,m2,d))
    print(f.prediction_eff_z(1,50,m1,m2,d))
    print(f.prediction_eff_z(1, 10,m1,m2,d))
    print(f.prediction_eff_z(1, 5,m1,m2,d))
    print(f.prediction_eff_z(1, 0,m1,m2,d))
    print(f.prediction_eff_z(1, -10,m1,m2,d))
    

    print("\n\n\n")

    print(f.prediction_eff_z(.5,1000,m1,m2,d))
    print(f.prediction_eff_z(.5,500,m1,m2,d))
    print(f.prediction_eff_z(.5,300,m1,m2,d))
    print(f.prediction_eff_z(.5,200,m1,m2,d))
    print(f.prediction_eff_z(.5,100,m1,m2,d))
    print(f.prediction_eff_z(.5,50,m1,m2,d))
    print(f.prediction_eff_z(.5, 10,m1,m2,d))
    print(f.prediction_eff_z(.5, 5,m1,m2,d))
    print(f.prediction_eff_z(.5, 0,m1,m2,d))
    print(f.prediction_eff_z(.5, -10,m1,m2,d))

    print("\n\n\n")

    print(f.prediction_eff_z(.1,1000,m1,m2,d))
    print(f.prediction_eff_z(.1,500,m1,m2,d))
    print(f.prediction_eff_z(.1,300,m1,m2,d))
    print(f.prediction_eff_z(.1,200,m1,m2,d))
    print(f.prediction_eff_z(.1,100,m1,m2,d))
    print(f.prediction_eff_z(.1,50,m1,m2,d))
    print(f.prediction_eff_z(.1, 10,m1,m2,d))
    print(f.prediction_eff_z(.1, 5,m1,m2,d))
    print(f.prediction_eff_z(.1, 0,m1,m2,d))
    print(f.prediction_eff_z(.1, -10,m1,m2,d))
    
    print("\n\n\n")

    print(f.prediction_eff_z(.00001,1000,m1,m2,d))
    print(f.prediction_eff_z(.00001,500,m1,m2,d))
    print(f.prediction_eff_z(.00001,300,m1,m2,d))
    print(f.prediction_eff_z(.00001,200,m1,m2,d))
    print(f.prediction_eff_z(.00001,100,m1,m2,d))
    print(f.prediction_eff_z(.00001,50,m1,m2,d))
    print(f.prediction_eff_z(.00001, 10,m1,m2,d))
    print(f.prediction_eff_z(.00001, 5,m1,m2,d))
    print(f.prediction_eff_z(.00001, 0,m1,m2,d))
    print(f.prediction_eff_z(.00001, -10,m1,m2,d))

    print("\n\n\n")
    print(f.prediction_eff_z(0,1000,m1,m2,d))
    print(f.prediction_eff_z(0,500,m1,m2,d))
    print(f.prediction_eff_z(0,300,m1,m2,d))
    print(f.prediction_eff_z(0,200,m1,m2,d))
    print(f.prediction_eff_z(0,100,m1,m2,d))
    print(f.prediction_eff_z(0,50,m1,m2,d))
    print(f.prediction_eff_z(0, 10,m1,m2,d))
    print(f.prediction_eff_z(0, 5,m1,m2,d))
    print(f.prediction_eff_z(0, 0,m1,m2,d))
    print(f.prediction_eff_z(0, -10,m1,m2,d))



# def prediction_GUI():
#     location = input("Enter Your Location: ")
#     la, lo = dasc.coords(location)

#     today = datetime.datetime.now()
#     d = datetime.timedelta(days = 10)
#     yesterday = datetime.timedelta(days = 1)
#     day_10 = today - d
#     yesterday = today-yesterday


#     yesterday = str(yesterday.date())
#     day_10 = str(day_10.date())



#     data = dasc.hist_data(yesterday, day_10, la, lo)

#     data = data['data']
#     #needed to strip the strings off the data
#     data = data.rstrip("'")
#     data = data.lstrip("'")
#     #coverts string to dict
#     data = ast.literal_eval(data)

    

#     rain = []
#     tempiture = []
#     humid = []
#     elevation = 0
#     for j in range(len(data['data'])):
#         elevation = data['data'][j][2]
#         rainfall = data['data'][j][4]*24
#         temp = data['data'][j][5]
#         humidity = data['data'][j][7]
        
#         rain.append(rainfall)
#         tempiture.append(temp)
#         humid.append(humidity)
    
#     c_rainfall = f.cumulative_rainfall(rain, tempiture, elevation, humid, la)

#     m1,m2,d = f.prediction_formula()

#     prediction_formatted_eff(c_rainfall, elevation, m1, m2, d)
            
def main():
    demo_cumulative_rainfall()

    demo_flood_prob_values()
#     # rainfall = demo_cumulative_rainfall()
#     # alt = 10
#     # demo_flood_prob(rainfall, alt)


#     #prediction_GUI()
if __name__ == '__main__':
    main()
