import math

def radToDeg(x):
    degrees = x * 180/math.pi
    return degrees

try:
    num = int(input("Enter a radian to convert into degrees: "))
    radNum = radToDeg(num)
    print("\tThe angle degree of the radian " + str(num) + " is " + str(radNum) + ".")
except ValueError:
    print("Please enter a valid integer value. ")