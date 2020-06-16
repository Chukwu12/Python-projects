Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from graphics import *
>>> win = GraphWin("Demo", 300,400)
>>> win.setCoords(0,0,3,4)
>>> circ = Circle(Point(1.5, 2),1)
>>> circ.draw(win)
Circle(Point(1.5, 2.0), 1)
>>> 
