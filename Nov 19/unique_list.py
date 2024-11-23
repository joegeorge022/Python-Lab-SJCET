'''
Author :
Date: November 19, 2024
'''
my_list=[1,2,3,4,3,2,4,2,3,5,2,6,2,4,6,5,4,6,6,4,6]

new_list=[]
duplicates=[]

for number in my_list:
    if number not in new_list:
        new_list.append(number)
        duplicates.append(number)

print(f"The original list is {my_list}")
print(my_list)
print(new_list)
print(duplicates)
