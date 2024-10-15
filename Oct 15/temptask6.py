'''
Python Lab
Author: Joe George
Date: October 15

Title: Find the smallest of 3 numbers
'''

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
num3 = int(input("Enter Number 3: "))


if num1<num2 and num1<num3:
    print("The given number",num1," is smallest.")
elif num2<num3 and num2< num1:
    print("The given number",num2,"is smallest.")
else:
    print("The given number",num2,"is smallest.")