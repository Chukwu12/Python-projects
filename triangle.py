# CSI 31 Okechukwu Egeruoh triangle.py
# Takes the sides of a triangle from the user and calculates the area if it can be a one if not requests the user to enter a set that does.
from math import*
def main():
    print("This Program is meant to calculate the area from the three sides of a triangle")
    print()
    a,b,c= eval(input("Please give 3 numbers for the side of the triangle with a comma between each:"))
    if c < a+b or a< b+c or b< a+c:
        a,b,c= eval(input("Please give 3 numbers for the side of the triangle with a comma between each:"))
    s = (a+b+c)/2
    area = sqrt(s*(s-a)*(s-b)*(s-c))
    print("The Area of the triangle is:",area)
main()
"""
This Program is meant to calculate the area from the three sides of a triangle

Please give 3 numbers for the side of the triangle with a comma between each:1,2,3
Please give 3 numbers for the side of the triangle with a comma between each:2,4,5
The Area of the triangle is: 3.799671038392666
>>> 
"""
