'''
Python Lab
Author: Joe George
Date: October 22

Title: Convert temperature values back and forth between Celsius and Fahrenheit.
'''

temp = int(input("Enter temperature: "))
Confirm = input("Is this in (C)elsius or (F)ahrenheit: ")

if Confirm == "C":
    print(temp,"Celsius is",temp*(9/5)+32,"Fahrenheit.")
elif Confirm == "F":
    print(temp, "Fahrenheit is ", 5 / 9 * (temp - 32), "Celsius.")
else:
    print("Unit is not valid")












