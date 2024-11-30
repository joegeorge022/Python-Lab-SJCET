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


