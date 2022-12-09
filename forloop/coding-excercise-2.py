'''Create a for loop to remove the duplicates in the following list :

lst = [ 'red', 'blue', 'yellow', 'black', 'red', 'blue', 'green', 'black', 'blue']
Do not use set() function'''

lst = [ 'red', 'blue', 'yellow', 'black', 'red', 'blue', 'green', 'black', 'blue']
lst_new = []
for i in lst:
    if i in lst_new:
        pass
    else:
        lst_new.append(i)
print(lst_new)