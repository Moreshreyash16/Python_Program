'''
@Author: Shreyash More

@Date: 2023-06-05 12:34:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-05 14:34:30

@Title : > Create a tic tac game 
'''
import random

def prn(arr):
    """
    Description:
        prints the array
    Parameter:
        Take array as a input
    Return:
       Prints the array
    """
    for i in arr:
        print(i)
def full(arr):
    """
    Description:
        Check if  the array is full or not
    Parameter:
        Take array as a input
    Return:
       Return full if array is full
    """
    for i in arr:
        if '_' in i:
            return False
    return True            

def computer(arr):
    """
    Description:
        The computer select the box using this function
    Parameter:
        Take array as a input
    Return:
       it does not returns anything 
    """
    while(True):
            computer_i=random.randint(0,2)
            computer_j=random.randint(0,2)
            if arr[computer_i][computer_j]!='O' and arr[computer_i][computer_j]!='X':
                arr[computer_i][computer_j]='O'
                break
def player(arr):
    """
    Description:
        The user select the box using this function
    Parameter:
        Take array as a input
    Return:
       it does not returns anything 
    """
    while(True):
            try:
                x=int(input("Enter row : "))
                y=int(input("Enter column : "))
                if arr[x][y]!='O' and arr[x][y]!='X':
                    arr[x][y]='X'
                    break
                else:
                    print("The box is already filled")
            except IndexError:
                    print("Enter valid number")    
def win(arr,value):
    """
    Description:
        This function checks if the player has won or not
    Parameter:
        Take array and a value as a input for checking 
    Return:
       it returns boolean value
    """
    # checking diagonal values
    if arr[0][0]==arr[1][1]==arr[2][2]==value:
            return True 
    # checking other diagonal values
    if arr[0][2]==arr[1][1]==arr[2][0]==value:
            return True
    # checking verical and horizontal colloums
    for i in range(3):
        if arr[i][0]==arr[i][1]==arr[i][2]==value:
            return True
        if arr[0][i]==arr[1][i]==arr[2][i]==value:
            return True
    return False 
def startgame():
    """
    Description:
        This function creates a board and with this function we can play the game
    Parameter:
        it does not take input
    Return:
       it does not returns anything 
    """
    rows=3
    cols=3
    arr = []
    x='X'
    o='O'
    for i in range(rows):
        arr.append(['_']*cols)
    while(True):
        if(full(arr)):
            print("The game is over")
            break    
        prn(arr)
        print("Enter value in box")   
        player(arr)
        print("computers turn")
        computer(arr)
        
        if win(arr,x): 
            prn(arr)
            print("winner is you Congrats!!!!!")
            break
        
        elif win(arr,o):
            prn(arr)
            print("winner is Computer !!!")
            break
        elif (win(arr,x)) and (win(arr,o)) or (full(arr)):
            print("it is a tie")
            break
def main():
    startgame()
if __name__=="__main__":
    main()
    
