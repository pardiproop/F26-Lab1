
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Pardip Rooprai
# Date: 18/9/2026
# Purpose: Use string methods and f-string formating.
# Usage: python3 lab1e.py

#TO-DO 1:
# Create a variable called "quantity".
# The value of "quantity" should be a decimal number of your own choice.
# Create another variable called "stock"
# The value of "stock" should also be a decimal number of your own choice.
# Print the product of `quantity` and `stock` with 4 spaces before the answer using the module % formatting.
# Then print the product of `quantity` and `stock` with 7 spaces before the answer and make sure the answer only goes to hundreadths (-.--) using the module % formatting.
quantity=3.5
stock=7.95
product=quantity*stock
print("The product is %4d" %(product))
print("The product is %7.2d" %(product))
print("The product is %15.2d" %(product))
print("The product is %4f" %(product))
print("The product is %7.5f" %(product))
print("The product is %15.5f" %(product))