'''
@Author: Shreyash More

@Date: 2023-06-03 15:34:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-05 12:34:30

@Title : Leap Year

''' 
# Taking year as input
year=int(input("Enter a year"))
if year>999 & year<10000:
    # condition to check it is divisible by 4
    if (year % 4) == 0: 
            # condition to check it is divisible by 100
            if (year % 100) == 0:
                # condition to check it is divisible by 400
                if (year % 400) == 0:
                    print("It is a leap year")
                else:
                    print("It is not a leap year")
            else:
                print("It is a leap year")
    else:
        print("It is not a leap year")