'''Print a list with capitalized elements in the lst list

lst = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
using for loop and capitalize() function'''

lst = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
cap_lst = []
for i in lst:
    i = i.capitalize()
    cap_lst.append(i)
print(cap_lst)