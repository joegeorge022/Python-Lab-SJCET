'''
Python Lab
Author: Joe George
Date: October 8

Title: Create, concatenate, and print a string and access a sub-string from a given string.
'''

first_name=input("Enter your first name")       #The first string containing first name.
last_name=input("Enter your last name")         #The second string containing last name.

full_name=first_name+" "+last_name              #Concatenated the two strings & store result in a new variable.
print(full_name)                                #Prints the concatenated string.

length= len(first_name)                         
print(length)
extracted_last_name=full_name[:length]          #Uses string slicing to extract the sub-string.
print(extracted_last_name)











