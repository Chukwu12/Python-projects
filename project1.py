# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

@author: Okechukwu Egeruoh
"""
# Write a program that receives a series of numbers from the user and
 #allows the user to press the designated key such as "No", or "End" to 
 #indicate that he or she is finished providing inputs. Upon the user finished 
 #entering the number, your program should provide the following statistics of 
 #the entered number how many numbers entered;
#the sum of numbers;
#the average of numbers;
#the smallest number;
#the largest number;

Sum = 0
i = 0
Count = 0
Number = []

#will loop until enter key is pressed
while True:

    data = input("Please enter a number and press Enter to quit: ")
    if data == '':

      #break loop
        break
    number = float(data)

    #sum plus numbered entered 
    Sum += number
    i += 1

print()

print("The sum equals", Sum)
if i > 0:

  #average calulation
    average = Sum / i
    print('The average equal', average)
         
 #Count Calulation
    Count = 0 
    avg = Count/i
    print("how many numbers entered", i)

NumList = []
Number = int(input("Please enter number: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d number : " %i))
    NumList.append(value)
print("The Min number is : ", min(NumList))
print("The Max number is : ", max(NumList))


