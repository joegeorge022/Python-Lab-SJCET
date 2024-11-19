'''
Author :
Date: November 19, 2024
'''

list1 = []
list2 = []

#Create list 1.
list1_size = int(input("Enter the size of list 1: "))
print("Enter the elements of list 1 :")
for i in range(list1_size):
    list1.append(int(input()))


#Create list 2.
list2_size = int(input("Enter the size of list 2: "))
print("Enter the elements of list 2 :")
for i in range(list2_size):
    list2.append(int(input()))


combined_list = list1 + list2

even_list=[]
odd_list=[]

for number in combined_list:
    if number%2==0:
        even_list.append(number)
    else:
        odd_list.append(number)

print(f"These are the odd numbers {odd_list}")
print(f"These are the even numbers {even_list}")

final_list = odd_list+even_list

print(f"The final list is {final_list}")