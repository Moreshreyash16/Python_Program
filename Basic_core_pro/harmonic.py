'''
@Author: Shreyash More

@Date: 2023-06-03 15:34:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-05 12:34:30

@Title : Prints the Nth harmonic number

'''
#Taking n as input
n = int(input("Enter the value of N \n"))
sum=0
# Calculating harmonic value till numbers
for i in range(1,n):
    sum+=1/i
#printing the values
print(f"the harmonic sum of {n} numbers is {sum}")