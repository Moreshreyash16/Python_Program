'''
@Author: Shreyash More

@Date: 2023-06-05 12:34:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-05 15:34:30

@Title : Simulates a gambler who start with $stake and place fair $1 bets until
he/she goes broke (i.e. has no money) or reach $goal. 
'''
import random

def gambling(stake,goal):
    """
    Description:
        It calculates the winning and losing percentage
    Parameter:
        Take two input first is stake i.e the amount you have for betting
        and second is goal i.e how much your target is
    Return:
       Prints the winiing and loosing percentage
    """
    win=0
    loss=0
    bet=0
    while(stake>=1):
        result=random.randint(0,1)
        if(stake>=goal):
            break
        elif(result==0): # 0 means loss
                stake-=1
                loss+=1
        else:           # 1 means win
                stake+=2
                win+=1    
        bet+=1      # counting the total amount of bet made 
    # calculating the win and loss percentage
    win_percentage=win/bet*100
    loss_percentage=100-win_percentage


    print(f"The loss percentage is : {'%0.2f'%loss_percentage}%")
    print(f"The win percentage is : {'%0.2f'%win_percentage}%")

def main():
    stake=int(input("Enter a Stake ammount : "))
    goal=int(input("Enter a goal ammount : "))
    n=int(input("Enter a number of times to run : "))
    for i in range(n):
        gambling(stake,goal)

if __name__ == "__main__":
    main()

