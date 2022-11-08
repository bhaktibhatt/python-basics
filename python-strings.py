#printing on new line 
str1 = 'Hello,\n\nIt\'s been a while but,\nHow are you?\n\nHave a nice day\njohn'
print(str1)

'''Slice and indice a string'''
str2 = 'Hello World!'
ind = str2[3:8]#does'nt include the last index
ind2 =  str2[0:6]
ind3 = str2[0:-1]

print(ind) 
print(ind2)
print('3rd string '+ind3)

str3 = "It is a nice day"
print(str3[8:])

'''Using same string for multiple output'''

Str = '''Master has failed more,
than the beginner has tried'''
print(Str)

'''string method/functions are accessed using dot(.) operator'''
print(str2.capitalize()) #upper case str2[0] only
print(str2.upper())
print(len(str2))
