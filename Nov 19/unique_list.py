'''
Author :
Date: November 19, 2024
'''
my_list = [0,0,1,2,3,3,2,3,4,5,3,6,7,8,7,9,8,9,10]
unique_list = []

for number in my_list:
    if number not in unique_list:
        unique_list.append(number)

print(f"The original list is {my_list}")
print(unique_list)
