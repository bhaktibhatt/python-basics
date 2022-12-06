'''
Q6.What is wrong in the following programs?
a = 4j + 54
b = int(a)

c = b + 6j+2
print(c)
i = 34
f = 45
c = 2y+5

print(i,f,c)
'''
# we can get real part of complex no not in
a =54 + 4j 
b = a.real
c = b + 6j+2
print(c)

i = 34
f = 45
c = 2j+5
#complex no imaginary part has val=riable j only
print(i,f,c)
