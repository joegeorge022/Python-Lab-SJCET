'''
Author: Joe George
Date: 30 November 2024
Check for valid mobile number

Rules for valid mobile number:
1. Every number should contain exactly 10 digits
2. The first digit should be 7 or 8 or 9
'''

mobile_number = input("Enter your mobile number: ")           # Asks the user to input their mobile number

if len(mobile_number)== 10 and mobile_number[0] in "789":     # Checks if the rules are satisfied.
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")
