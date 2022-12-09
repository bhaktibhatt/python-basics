def greet(name):
    print('Hemlo '+str(name))

greet('Mac')

def desg(name, designation):
    print('Name: '+str(name))
    print('Designation: '+str(designation))

desg(designation='Junior developer',name = 'Jake') #keyword argument
desg('Khushi','UI/UX designer') #positional argument


def result(name='None',marks = None):
    if name != 'None' or marks != None:
        print('Name: '+str(name))
        print('Marks: '+str(marks))
result(marks=99)

#to pass any no of arguments
def add(*n):
    sm = 0
    for i in n:
        sm += i
    return sm

a1 = add(10,20,40)
print(a1)
add(2,4)
add(8)

#arbitary keywords we dont know what to pass this will return a dictionary
def info(**kw):
    for k,v in kw.items():
        print(k, ':', v)
    
info(name='Bhakti',age='20', todo = 'Study')


#A lambda function can take any number of arguments, but can only have one expression.
sub = lambda n, m : n - m

print(sub(40,10))

#redefining type function

def type_dt(data):
    dt = str(type(data))

#function to add nos and print ans upto min decimal value from nos
def sum_round(*n):
    sm = 0
    d = []
    for i in n:
        sm += i
        num = str(i).split('.')
        d.append(len(num[1]))

    return round(sm, min(d))

print(sum_round(2.12,455.5677))
print(sum_round(45.891, 4542.99003, 45321.993))