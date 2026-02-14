"""
Problem Statement: Write a Python Program that:
1. Ask the user for a number as input .
2. Uses the math module to calculate the :
    1. Square root of the number
    2. Natural Logarithm (log base e)of the number
    3. Sine of the number (in radians)

3. Display the calculation result
"""
import math


number = int(input("Enter a number: "))
e_value=math.e
square_root = math.sqrt(number)
logarithm_root = math.log(number,e_value)
sine_root = math.sin(math.radians(number))

print(f"the square root of {number} is {square_root}")
print(f"the logarithm of {number} is {logarithm_root}")
print(f"the sine of {number} is {sine_root}")