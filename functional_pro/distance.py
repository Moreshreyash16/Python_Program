'''
@Author: Shreyash More

@Date: 2023-06-04 18:34:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-05 12:34:30

@Title : Write a program Distance.java that takes two integer command-line arguments x
and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0).

'''
import math

def distance_calculator(x,y):
    """
Description:
    It calculates the distance using sqrt function from math module
Parameter:
      Takes x,y as parameters for calculating distance
Return:
       Returns the calculated distances
"""
    distance=math.sqrt(x*x + y*y)
    return distance
def main():
    # Taking x y input forom user to calculate Distance
    x=int(input("Enter x co-ordinate : "))
    y=int(input("Enter y co-ordinate : "))
    # Calling the Function and Printing the Value
    print(distance_calculator(x,y))

if __name__=="__main__":
    main()