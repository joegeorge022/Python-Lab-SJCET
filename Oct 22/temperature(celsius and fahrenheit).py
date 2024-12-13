'''
Python Lab
Author: Joe George
Date: October 22

Title: Convert temperature values back and forth between Celsius and Fahrenheit.
'''

temp = int(input("Enter temperature: "))                                          #Asks the user to enter input
Unit = input("Is this in (C)elsius or (F)ahrenheit: ")                         #Checks if temperature is in Celsius or Fahrenheit.

if Unit == "C"or Unit == "c":
    print(temp,"Celsius is",temp*(9/5)+32," Fahrenheit.")                         #Converts Celsius to Fahrenheit.
elif Unit == "F"or Unit == "f":
    print(temp, "Fahrenheit is ", 5 / 9 * (temp - 32), "Celsius.")                #Converts Fahrenheit to Celsius.
else:
    print("Unit is not valid")                                                    #You entered the wrong unit.






