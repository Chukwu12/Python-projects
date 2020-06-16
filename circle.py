# CSI 31 James Stefanik circle.py
# Takes a radius from the user and displays a circle it along with a line going through the y intercept.
from graphics import*
from math import*
def main():
    win=GraphWin("circle",200,200)
    win.setCoords(-10,-10,10,10)
    print("This program takes a radius from the user and displays a circle and a line running through it using the y-intercept")
    print()
    rad = eval(input("Please give the radius of the circle: "))
    y = eval(input("Please give the y-intercept: "))
    circle = Circle(Point(0,0),rad)
    circle.draw(win)
    x= sqrt(rad**2 -y **2)
    line = Line(Point(-10,y),Point(10,y))
    line.draw(win)
    pt1=Circle(Point(-x,y),.25)
    pt1.setFill("red")
    pt1.setOutline("red")
    pt1.draw(win)
    pt2=Circle(Point(x,y),.25)
    pt2.setFill("red")
    pt2.setOutline("red")
    pt2.draw(win)
main()
"""
This program takes a radius from the user and displays a circle and a line running through it using the y-intercept

Please give the radius of the circle: 5
Please give the y-intercept: 3
"""
