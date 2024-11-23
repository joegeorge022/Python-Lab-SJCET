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
for k in range(num+1):
    for c in range(num-k):  
        print(" ", end="")
    for f in range(1, 2*k): 
        print("*", end="")
    print()  

# Inverted Hill Pyramid
for q in range(num, 0, -1):
    for d in range(num-q):  
        print(" ", end="")
    for e in range(1, 2*q):  
        print("*", end="")
    print()
