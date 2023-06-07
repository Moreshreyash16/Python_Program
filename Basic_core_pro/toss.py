'''
@Author: Shreyash More

@Date: 2023-06-03 15:34:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-05 12:34:30

@Title : Flip Coin and print percentage of Heads and Tails

'''
import random
# Taking input for number of times to flip
flip_number=int(input("How many times you want to flip \n"))
result=random.randint(0,1)
heads=0
tails=0
# Checking if it is head or tails
if result==0: # 0 Represent heads
    heads+=1
else:         # 1 Represent tails
    tails+=1
# Calculating wining percentage
win_percent_heads=((heads/flip_number)*100)
win_percent_tails=100-win_percent_heads
print(f"winning percentage of heads is {win_percent_heads} " + "\n" + "winning percentage of tail is {win_percent_tails} ")