'''
Python Lab
Author: Joe George
Date: October 22

Title: Find the largest of 3 numbers
'''

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
num3 = int(input("Enter Number 3: "))


if num1>=num2 and num1>=num3:
    print("The given number",num1," is largest.")
elif num2>=num3 and num2>=num1:
    print("The given number",num2,"is largest.")
else:
    print("The given number",num3,"is largest.")



















