'''Create a program to clear the lst list

lst = [ 1, 4, 56, 2, 4 , 12,  6, 89 ,11, 0]
Using while loop and pop() function only.

Also print the empty list'''

lst = [ 1, 4, 56, 2, 4 , 12,  6, 89 ,11, 0]

while lst:
    lst.pop()
print(lst)