'''
8 October PART-1

Title: Simple desktop calculator using Python. Only the five basic arithmetic operators.

AIM: Write a Python program that performs the following tasks:

    User Input:
        Ask the user to enter two numbers, num1 and num2.
        Ask the user to enter a third number, num3.

    Addition:
        Add the first two numbers (num1 and num2).
        Print the sum in the format: "The sum of num1 and num2 is: result"

    Subtraction:
        Subtract num2 from num1.
        Print the difference in the format: "The difference when num2 is subtracted from num1 is: result"

    Multiplication:
        Multiply num1 by num2.
        Print the product in the format: "The product of num1 and num2 is: result"

    Division:
        Divide num1 by num2. Ensure that division by zero is handled properly.
        Print the quotient in the format: "The quotient when num1 is divided by num2 is: result"

    Modulus:
        Find the remainder when num1 is divided by num2.
        Print the remainder in the format: "The remainder when num1 is divided by num2 is: result"

    Combined Arithmetic Operation:
        Perform the following combined operation:
        result = (num1 + num2) * num3 / 2
        Print the result in the format: "The result of (num1 + num2) * num3 / 2 is: result"

Title: Create, concatenate, and print a string and access a sub-string from a given string.

Write a Python program that performs the following tasks:

    Create two separate strings:
        The first string should contain your first name.
        The second string should contain your last name.

    Concatenate the two strings with a space in between and store the result in a new variable.

    Print the concatenated string.

    From the concatenated string:
        Access and print a sub-string that consists of the last name only. Use string slicing to extract the sub-string.

Example:

If the first name is "John" and the last name is "Doe", the concatenated string should be "John Doe". The sub-string should be "Doe".
'''



'''
8 October - PART 2
Title: Familiarize time and date in various formats (Eg. “Thu Jul 11 10:26:23 IST 2024”).

Familiarize time and date in various formats (Eg. “Thu Jul 11 10:26:23 IST 2024”).

Display current date and time
Display the format  [YYYY-MM-DD HH:MM:SS]
Display the format  [MM/DD/YYYY]
Display the format  [Day, Month DD, YYYY]
Display the format  [Day, Month DD, YYYY HH:MM:SS AM/PM]
Format the date and time like "Thu-Jul-11 10:26:23 IST 2024"
Display [Abbr Weekday Name-Abbr month name-DD HH:MM:SS IST YYYY]  Eg: Wed-Oct-02 12:41:18 IST 2024
Display format- 8 [ISO format:]
Display Date only
Display Time only
Display month only
Display Year only
Theory

-To work with time and date in various formats in Python, you can use the datetime module.

-This module allows you to format dates and times in different ways using strftime() and parse them using strptime().

Commonly Used Date and Time Format Codes

%a: Abbreviated weekday name (e.g., Mon, Tue)
%A: Full weekday name (e.g., Monday, Tuesday)
%b: Abbreviated month name (e.g., Jan, Feb)
%B: Full month name (e.g., January, February)
%d: Day of the month (zero-padded) (e.g., 01, 02, 31)
%m: Month as a zero-padded decimal number (e.g., 01, 02, 12)
%Y: Year with century (e.g., 2024)
%H: Hour (24-hour clock) (e.g., 00, 23)
%I: Hour (12-hour clock) (e.g., 01, 12)
%M: Minute as a zero-padded decimal number (e.g., 00, 59)
%S: Second as a zero-padded decimal number (e.g., 00, 59)
%p: AM or PM
%Z: Time zone name (e.g., IST, UTC)
from datetime import datetime
current=datetime.now() #datetime.now() returns the current local date and time
print(current)
#(b)    Display the format  [YYYY-MM-DD HH:MM:SS]
format_1=current.strftime("%Y-%m-%d %H:%M:%S")
print("format -1 [YYYY-MM-DD HH:MM:SS]::--->",format_1)
'''
