'''
Author: Joe George
Date: 30 November 2024
Sum Function
'''

# 1. Input is given as parameters by the user when calling the function.
def sum(num1,num2):                       # Here sum() is the function and the parameters are num1 & num2
    result = num1 + num2                  # Adds the 2 numbers.
    return result                         # Returns the result.

print(sum(3,4))              #Prints the sum of 3 & 4


# 2. Input is collected separately from the user
def addition():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 + num2
    return result

print(f"The sum of the two numbers is: {addition()}")
