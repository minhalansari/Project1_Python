    #########################################################
    #  Computer Project #1
    #
    #  Algorithm
    #    prompt for rods
    #    input a rods
    #    print rods
    #       convert to meters
    #       print meters
    #       convert to feet	
    #        print feet
    #       convert to miles
    #      print miles
    #      convert to furlong
    #      print furlong
    #      convert to minutes
    #      print minutes to walk
    ###########################################################
Created on Sun Sep 10 00:08:43 2017

@author: minhalansari
"""

rods_str= input('Input rods: ')
rods_float= float(rods_str)
print("You input", rods_float, "rods." )
print("Conversions")
meters_int = (rods_float*5.0292)
print("Meters: ",round( (meters_int),3))
feet_int= (meters_int/0.3048)
print("Feet: " , round((feet_int),3))
miles_int= (meters_int/1609.34)
print("Miles: ", round((miles_int),3))
furlong_int= (rods_float /40)
print("Furlongs: ", round((furlong_int),3))
minutes_int = ((miles_int*60)/3.1)
print("Minutes to walk",rods_float, "rods: " , round((minutes_int),3))
 
