#
import math

def intro():
    print("This program computes the surface area and the volume of sphere.")
    return
def getRadius():
    r = float(input("Enter the radius of the shpere:"))
    return r
def sphereArea(radius):
    area = 4*math.pi*radius**2
    return area
def sphereVolume(radius):
    volume = (4/3)*math.pi*radius**3
    return volume


def main():
    intro()
    radius = getRadius()
    s_area = sphereArea(radius)
    vol = sphereVolume(radius)
    
    print("The surface area is:",s_area,"and the volume is:", vol)

main()
      
    
    
