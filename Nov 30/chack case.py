'''
Author: Joe George
Date: 30 November 2024
Checks for the number of Uppercase & Lowercase characters in a string.
'''


string_input = input("Enter your string: ")

# Sets the value of number of Uppercase & Lowercase characters = 0 at beginning
upper_count = 0
lower_count = 0

#
for i in range(len(string_input)):
    if  string_input[i].isupper() is True:    # This conditional checks for uppercase letters
        upper_count +=1     #Adds +1 to number of Uppercase characters
    else:
        lower_count +=1     #Adds +1 to number of lowercase characters

print(f"The number of Uppercase characters in the string is: {upper_count}")
print(f"The number of lowercase characters in the string is: {lower_count}")
