'''In a shopping mart, a person bought items of following prices,

lst = [ 110, 65, 245, 80, 200, 115, 455]
use a for loop to calculate the sum of the elements using the + operator in the list and print it

*without using sum() function'''
lst = [ 110, 65, 245, 80, 200, 115, 455]
sum = 0
for i in lst:
    sum += i
print(sum)