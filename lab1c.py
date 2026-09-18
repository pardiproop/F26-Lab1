
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Pardip Rooprai
# Date: 18/9/2026
# Purpose: Use string methods and f-string formating.
# Usage: python3 lab1c.py

#TO-DO 1:
# import math module.
# Create a variable called 'radius' and take its value form user.
# Convert the variable to integer using int()
# use the constant pi form math module and compute the area of the circle using the variable 'radius'
import math
radius=int(input("Please Enter the Radius of Circle: "))
area=math.pi*radius**2
print("area=", area)
