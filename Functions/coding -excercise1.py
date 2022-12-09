'''Create a function dsort() to sort a list in descending order, 
taking a list as argument and returning it
Use the following list and print it!'''

lst = [ 5, 6, 7, 23 ,12 ,3, 3, 4 ,5, 12, 34]
def dsort(l):
    l.sort(reverse = True)
    return l
print(dsort(lst))