'''
Python Lab
Author: Joe George
Date: October 22

Title: Find the largest of 3 numbers
'''

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
num3 = int(input("Enter Number 3: "))


if num1>=num2 and num1>=num3:                                    #Checks if 1 is the largest number
    print("The given number",num1," is largest.")
elif num2>=num3 and num2>=num1:                                  #Checks if 2 is the largest number
    print("The given number",num2,"is largest.")
else:                                                            #If neither 1 nor 2 is the largest number then 3 is the largest number
    print("The given number",num3,"is largest.")



















