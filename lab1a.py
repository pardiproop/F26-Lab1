# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Pardip Rooprai
# Date: 18/9/2026
# Purpose: Create a variable, check its type and print the variable.
# Usage: python3 lab1a.py


# TO DO 1: Creating and using varibales
# create a variable called message.
# Set the variable to equal to "Welcome to PRG101".
# Print the variable message using print() statement.
message="Welcome to PRG101" # this prints a welcome message to the user
print(message) # this is the print message function/feature

# TO DO 2: Checking the type of a varibale
# Use the builtin type() function and print the type of this variable.
print(type(message)) # this prints the type of message
newstring=message+"Python is the Future"
print(newstring)
# Another way to print this message is by writing: print(message+"Python is the Future")

# TO DO 3: Dynamic Typing:
# Create a varibel called `x` and assign it the value 10, then print the type of this variable.
x=10
print(type(x))

# TO DO 4: Dynamic Typing: 
# Now reassign a new value to the variable `x`, this value should be a string, e.g "hello", check the type of the variable `x` again.
x="hello"
print(type(x))

# What did you observe?
# (1) There are two ways the user can print "Python is the Future" by either using newstring as a variable and printing it or having message varible in brackets to print the message.
# (2) The value "x" got assigned to two variables and changed from integer to string without assigning or creating a new value or variable.
