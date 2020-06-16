# CSI 31 James Stefanik distance.py
# Takes coordinates from the user then finds and displays the distance between them.
from math import*
def main():
    print("This program will take 2 coordinates from you and give you the distance of the ponits")
    print()
    x1, y1 = eval(input("please give x,y coordinates for the 1st ponit with a comma in between: "))
    x2, y2 = eval(input("please give x,y coordinates for the 2nd ponit with a comma in between: "))
    distance= sqrt(((x2-x1)**2)+((y2-y1)**2))
    print("The distance between the to ponits is",distance)
main()
"""
This program will take 2 coordinates from you and give you the distance of the ponits

please give x,y coordinates for the 1st ponit with a comma in between: 2,3
please give x,y coordinates for the 2nd ponit with a comma in between: 4,5
The distance between the to ponits is 2.8284271247461903
>>> 
"""
