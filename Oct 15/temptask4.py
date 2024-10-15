'''
Python Lab
Author: Joe George
Date: October 15

Title: Apply discount based on total purchase amount
'''

price = int(input("Enter the total purchase amount: "))

if price < 200:
    print("No discount applied. Cost= $",price)
elif price<=500:
    print("10% discount applied. Cost= $",price - price/10)
else:
    print("20% discount applied. Cost= $",price - price/20)


















