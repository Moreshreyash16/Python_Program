'''
@Author: Shreyash More

@Date: 2023-06-05 12:34:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-05 14:34:30

@Title : > Given N distinct Coupon Numbers
'''

import random

def coupon_number(n):
    """
    Description:
        It genrates a 9 digit coupon number
    Parameter:
        Takes a integer as input for genrating n number of coupon
    Return:
       Returns array of distinct coupon
    """
    arr=[]
    for i in range(n):
        # generating a 9 digit coupon
        num=random.randint(100000000,999999999)
        # cheking if it is distinct or not
        if num not in arr:
            arr.append(num)
    return(arr)

def main():
    num=int(input("Enter value to genrate coupons "))
    coupon=coupon_number(num)
    # printing the coupon
    for j in coupon:
        print(j)        

if __name__=="__main__":
    main()