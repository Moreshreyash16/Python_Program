'''
@Author: Shreyash More

@Date: 2023-06-03 15:34:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-05 12:34:30

@Title : Power of 2

'''
#Taking power as input
num = int(input("Enter the value of N \n"))
if(num<=31):
        for i in range(1,num):   
            #Calcualting the power of 2
            table_of_num=2**i
            # printing the values
            print(f"The value of 2*{i} {table_of_num}")
