'''
Author:
Date: November 19, 2024
'''
num = int(input("Enter a number: "))

# Increasing Triangle
for i in range(num+1):
    for a in range(i):  
        print("*", end="")
    print()  

# Decreasing Triangle
for j in range(num, 0, -1):
    for b in range(j):  
        print("*", end="")
    print()  

# Hill Pyramid
for i in range(num+1):
    for j in range(num-i):  
        print(" ", end="")
    for k in range(1, 2*i): 
        print("*", end="")
    print()  

# Inverted Hill Pyramid
for q in range(num, 0, -1):
    for d in range(num-q):  
        print(" ", end="")
    for e in range(1, 2*q):  
        print("*", end="")
    print()
