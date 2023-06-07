'''
@Author: Shreyash More

@Date: 2023-06-04 18:34:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-05 12:34:30

@Title : Sum of three Integer adds to ZERO
'''
import itertools

def sum_of_three(arr):
    """
    Description:
        It checks the combination of 3 from array of n numbers and check if the sum
        of combination are zero using combination function from itertools 
    Parameter:
        Takes an array of n number as input 
    Return:
       Returns the combination
    """
    comb=[]
    for c in itertools.combinations(arr, 3):
        comb.append(c)
    for i in comb:
        # Checking if the sum is zero
        if sum(i)==0:
            # returning the value if combination found
            return (f"Combination found {i}")
        else:
            return ("No Combination found")

def main():
    # Taking input from user
    n=int(input("Enter a Number: "))
    arr=[]
    # creating array of n numbers 
    for i in range(n):
        num=int(input("Enter a Value: "))
        arr.append(num)
    # calling and printing the value
    print(sum_of_three(arr))

if __name__=="__main__":
    main()