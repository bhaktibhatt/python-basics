'''
Q3.Given a string,
Str = 'John Smith'
create a program to generate the following outputs
using string operations:
john smith
JHON SMITH
J
th
Smith
hon
10

'''

Str = 'John Smith'
print(Str.lower())
print(Str.upper())
print(Str[0])
print(Str[-2:])
print(Str[2]+Str[1]+Str[3])
print(len(Str))