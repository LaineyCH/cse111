"""
The size of a car tire in the United States is represented with three numbers like this: 205/60R15. 
The first number is the width of the tire in millimeters. The second number is the aspect ratio. 
The third number is the diameter in inches of the wheel that the tire fits. 
The volume of space inside a tire can be approximated with this formula:

v = (PI * (w**2) * a * ((w * a) + (2540 * d))) / 10000000000

v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.
"""

import math

# collect user inputs and save to variables
width = float(input("Please enter the tire's width in mm (eg 205): "))
aspect = float(input("Please enter the tire's aspect ratio (eg 60): "))
diameter = float(input("Please enter the tire's diameter in inches (eg 15): "))

# calculate volume according to goven formula for volume
volume = (math.pi * (width**2) * aspect * ((width * aspect) + (2540 * diameter))) / 10000000000

# print volume
print(f"The volume of the tire is {volume: .2f} liters")