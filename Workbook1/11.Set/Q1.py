'''Q1.What will be the output of the following program?
a = {10, 20,30,40,50,60,70}
b = {33, 44, 51,10, 20, 50, 30, 33}
print(a 1 b)
print(a & b)
print(a - b)
print(b -a)
print(a A b)
print(a >= b)
print(a <= b)
'''
a = {10, 20,30,40,50,60,70}
b = {33, 44, 51,10, 20, 50, 30, 33}
print(a | b) #union
print(a & b) #intersection
print(a - b) #differnce
print(b - a) 
print(a ^ b) #symmetric difference
print(b ^ a)
print(a >= b)
print(a <= b)


'''
Q2.What is the difference between discard () & remove()
'''

'''
==> remove() takes key and delete the value at the key set is unordered hence remove is invalid function in set
==> discard() discards using value hence we use it in sets
'''

'''
Q3.Which operator is used to determine whether a set is a subset of another set?'''

'''==> use issubset() returns true is a set is a subset of another subset else false'''
A = {1,2,3}
B = {1,2,3,4,5}
print(A.issubset(B))

'''Q5.Why slice syntax doesn't work on sets? Write program to see what error you get.'''
'''
==> Because set is unordered you cannot slice it
'''