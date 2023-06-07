'''
@Author: Shreyash More

@Date: 2023-06-03 15:34:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-05 12:34:30

@Title : Prime Factors

'''
# Taking number as input
num=int(input("Enter a number "))
while(num>1):    
    for i in range(2,num+1): 
        if num%i == 0:
            #replacing the currrent num value by new value
            num = int(num/i)
            # printing the factors
            print(f"factors are {i}")
            break
