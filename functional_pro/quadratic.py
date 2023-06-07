'''
@Author: Shreyash More

@Date: 2023-06-04 18:34:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-05 12:34:30

@Title :Write a program Quadratic.java to find the roots of the equation a*x*x + b*x + c.
'''
import math

def quadratic_solver(a,b,c):
    """
    Description:
        It calculates the roots of equation using the the formula
    Parameter:
        Takes a,b,c as parameters for calculating the roots of X
    Return:
       Returns the two roots of X
    """
    delta=b*b - 4*a*c
    root_x1 = (-b + math.sqrt(delta))/(2*a)
    root_x2 = (-b - math.sqrt(delta))/(2*a)
    return (f"Root of x1 is {root_x1} Root of x2 is {root_x2}")
def main():
     # Taking a b c input forom user to calculate roots of X
    a=int(input("Enter value for a: "))
    b=int(input("Enter value for b: "))
    c=int(input("Enter value for c: "))
     # Calling the Function and Printing the Value
    print(quadratic_solver(a,b,c))

if __name__ == "__main__":
    main()