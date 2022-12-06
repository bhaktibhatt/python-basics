'''
Q5.What will be the output of the following program?
r i Str = 'python is easy'
2 a = Str.capitalize()
3 b = Str.upper()
4 c = Str. replace('easy', ' not tough')
5 d = Str.find('Easy')
6 e = Str[:7]
7 f = Str[11]
8 g = Str[2] + Str[-3:-1]\
9 + Str[2] + Str[l]
10 h = chr(72) + chr(97) + chr(67)\
11 + chr(75) + chr(101) + chr(100)
12 ■1 = '\x65\x6E\x64'
13 all = a+'\n'+b+'\n'+c+'\n'+str(d)+'\n ''\
14 +e+'\n'+f+'\n'+g+'\n'+h+'\n'+i
I 15 print(d)
'''
Str = 'python is easy'
a = Str.capitalize()
print('a:',a)
b = Str.upper()
print('b:',b)
c = Str. replace('easy' ,' not tough')
print('c:',c)
d = Str.find('Easy')
print('d:',d)
e = Str[:7]
print('e:',e)
f = Str[11]
print('f:',f)
g = Str[2] + Str[-3:-1]\
    + Str[2] + Str[1]
print('g:',g)
h = chr(72) + chr(97) + chr(67)\
    + chr(75) + chr(101) + chr(100)
print('h:',h)
i= '\x65\x6E\x64'
print('i',i)
all = a+'\n'+b+'\n'+c+'\n'+str(d)+'\n'\
+e+'\n' +f+ '\n' +g+ '\n' +h+ '\n' +i
print('\nall:',all)
print('d:',d)
