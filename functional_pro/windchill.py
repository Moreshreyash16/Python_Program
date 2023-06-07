'''
@Author: Shreyash More

@Date: 2023-06-04 18:34:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-05 12:34:30

@Title : Write a program WindChill that takes two double command-line arguments t
and v and prints the wind chil

'''
def wind_chill(temp, wind_speed):
    """
    Description:
        It calculates windchill using given formula
    Parameter:
        Takes an temperature and wind speed as input for calculating windchill
    Return:
       Returns windchill
    """
    if temp > 50 or wind_speed < 3:
        return temp 
    windchill = 35.74 + (0.6215 * temp) - (35.75 * wind_speed ** 0.16) + (0.4275 * temp * wind_speed ** 0.16)
    return windchill
# Taking temperature and wind speed as input
temperature = float(input("Enter temperature in Fahrenheit: "))
wind_speed = float(input("Enter wind speed in miles per hour: "))

# storing the calculated wind chill in varialable
wind_chill_cal = wind_chill(temperature, wind_speed)
# printing the wind chill
print("Wind chill factor:","%0.2f"% wind_chill_cal)