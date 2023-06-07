'''
@Author: Shreyash More

@Date: 2023-06-05 12:34:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-05 12:34:30

@Title : Write a Stopwatch Program for measuring the time that elapses between
the start and end clicks

'''
import time

start = time.time()

print("Enter 1 to start timer ")
num=int(input("Enter a choice"))
print("Enter 2 to stop Timer")
num=int(input("Enter a choice"))
end = time.time()
print(str(end - start)+"sec")