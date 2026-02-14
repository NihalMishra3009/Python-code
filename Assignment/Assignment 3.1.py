"""
Problem Statement : Write a Python program that
    1. Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion
    2. Returns the calculated factorial
    3. Calls the function with a sample number and prints the output.
"""
#Expected Output:
# For example if the function is called with 5, it should return:

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

number = int(input("Enter a number: "))
print(f"Factorial of {number} is {factorial(number)}")