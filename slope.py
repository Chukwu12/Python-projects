# Okechukwu Egeruoh.py
# calculates the slope of a line through two non-vertical points

def main():
    x1,y1 = eval(input("Please enter the (x1,y1) coordinates: "))
    x2,y2 = eval(input("Please enter the (x2,y2) coordinates: "))
    slope = (y2-y1)/(x2-x1)
    if x2 == x1:
        print ("enter the coordinates of a vertical line that has no slope")
        slope = 0
    slope = (y2-y1)/(x2-x1)
    print(" the slope between the two lines is ", slope)
main()
"""Please enter the (x1,y1) coordinates: 4,5
Please enter the (x2,y2) coordinates: 2,4
 the slope between the two lines is  0.5
>>> """
