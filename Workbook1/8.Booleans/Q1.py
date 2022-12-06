'''
QI.What will be the output of the following program?

a = 'Python'
b, c = 1059876,1058876

print(bool(b > c))
print(bool(not(b == c)))
print(bool('py' in a))
print(bool(int((str(b))[1])))
'''
a = 'Python'
b, c = 1059876,1058876

print(bool(b > c)) #false
print(bool(not(b == c))) #true
print(bool('py' in a)) #false
print(bool(int ( ( str(b)) [1] ) )) 