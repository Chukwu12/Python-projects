# CSI 31 Okechukwu Egeruoh squareroot.py
#This program takes a square root and the times to improve the guess from the user to find the square root and improved guess
from math import*

def main():
    print("This program takes a square root and the times to improve the guess from the user to find the square root and improved guess")
    x = eval(input("What is the square root you want to find? "))
    improve = eval(input("How many times do you want to improve your guess? "))
    guess = x/2
    for i in range(improve):
        if i== 0:
            guess = x/2
        guess = guess + ((x/guess)/2)
  
    guess = sqrt(guess)
    difference = x - guess
    print("The root of",x,"is approximately",guess)
    print("The difference between",x,"and the square of",round(guess,2),"is",round(difference,2))
main()
"""
This program takes a square root and the times to improve the guess from the user to find the square root and improved guess
What is the square root you want to find? 17
How many times do you want to improve your guess? 5
The root of 17 is approximately 3.5609858223459385
The difference between 17 and the square of 3.56 is 13.44
"""
