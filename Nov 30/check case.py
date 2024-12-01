'''
Author: Joe George
Date: 30 November 2024
Checks for the number of Uppercase & Lowercase characters in a string.
'''


string_input = input("Enter your string: ")

# Sets the value of number of Uppercase & Lowercase characters = 0 at beginning
upper_count = 0
lower_count = 0
number_count = 0
space_count = 0

for i in range(len(string_input)):
    if  string_input[i].isupper() is True:    # This conditional checks for uppercase letters
        upper_count +=1     #Adds +1 to number of Uppercase characters.
    elif string_input[i].islower() is True:
        lower_count +=1     #Adds +1 to number of lowercase characters.
    elif string_input[i].isnumeric() is True:
        number_count +=1    #Adds +1 to number of numeric characters.
    elif string_input[i].isspace() is True:
        space_count +=1     #Adds +1 to number of spaces.

print(f"The number of Uppercase characters in the string is: {upper_count}")
print(f"The number of lowercase characters in the string is: {lower_count}")
print(f"The number of Numeric characters in the string is: {number_count}")
print(f"The number of spaces in the string is: {space_count}")
