'''
Author: Joe George
Date: 30 November 2024
Checks if the function is right angled triangle or not
'''

def right_triangle():
    side1= int(input("Enter the length of 1st side: "))
    side2= int(input("Enter the length of 2nd side: "))
    side3= int(input("Enter the length of 3rd side: "))

    # The below lines of code checks if the Pythagorean Theorem is satisfied or not.
    if (side3) ** 2 == (side1) ** 2 + (side2) ** 2:
        return "The triangle is a right triangle."
    elif (side2) ** 2 == (side1) ** 2 + (side3) ** 2:
        return "The triangle is a right triangle."
    elif (side1) ** 2 == (side2) ** 2 + (side3) ** 2:
        return "The triangle is a right triangle."
    else:
        return "The triangle is NOT a right triangle."

print(right_triangle())



















"""
QUESTION
Program to check whether the given number is a valid mobile number or not using functions.

Rules:
1. Every number should contain exactly 10 digits.
2. The first digit should be 7 or 8 or 9
.................................................................................................................................................................................................................................

A program that accepts the lengths of three sides of a triangle as inputs. The program should output whether or not the triangle is a right triangle (Recall from the Pythagorean Theorem that in a right triangle, the square of one side equals the sum of the squares of the other two sides). Implement using functions.


"""
