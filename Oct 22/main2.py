'''
Python Lab
Author: Joe George
Date: October 22

Title: Convert temperature values back and forth between Celsius and Fahrenheit.
'''

temp = int(input("Enter temperature: "))                                          #Asks the user to enter input
Confirm = input("Is this in (C)elsius or (F)ahrenheit: ")                         #Checks if temperature is in Celsius or Fahrenheit.

if Confirm == "C"or Confirm == "c":
    print(temp,"Celsius is",temp*(9/5)+32," Fahrenheit.")                         #Converts Celsius to Fahrenheit.
elif Confirm == "F"or Confirm == "f":
    print(temp, "Fahrenheit is ", 5 / 9 * (temp - 32), "Celsius.")                #Converts Fahrenheit to Celsius.
else:
    print("Unit is not valid")                                                    #You entered the wrong unit.






