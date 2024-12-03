"""
Author: Joe George
Date: 3 December 2024
Function to print Fibonacci number until n.
"""

def fibonacci():
    n = int(input("Enter the range: "))
    previous2 = 0
    previous1 = 1
    print(previous2)
    print(previous1)

    for i in range(n):
        next_number = previous1 + previous2
        previous2 = previous1
        previous1 = next_number
        print(next_number)

print(fibonacci())