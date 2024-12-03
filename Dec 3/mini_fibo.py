"""
Author: Joe George
Date: 3 December 2024
Function to print Fibonacci number until n.
"""

def fibo(n):
    sequence = [0]
    num1,num2 = 0,1
    for i in range(n):
        num2,num1 = num1+num2,num2
        sequence.append(num2)
    return sequence

print(fibo(1))
