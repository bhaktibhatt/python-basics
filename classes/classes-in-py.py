class Coder():
    #self is a variable denoting class Coder
    #for a constructor self and name are parameters so while creating a object of this class we can pass name as a parameter as specified
    def __init__(self, name):#constructor
        self.Name = name
    def info(self):
        print(self.Name)
    def is_Pythonner(self):
        if 'Python' in self.language:
            print(True)
        else:
            print(False)

cd = Coder('Jake') #assign a object to class Coder and value for name is Jake as we gave name as parameter
cd.info()
print(cd.Name)

cd.language = ['Python','C','JS'] #language is a attribute added outside the class Coder
print(cd.language)
cd.is_Pythonner()
cd.language = ['C','JS']
cd.is_Pythonner()
cd.age = [20,30,25,26,22]
print(cd.age)

class Algebra():
    def __init__(self,r = 0.0, i = 0.0):#real, imag
        self.real = r
        self.imag = i
    def __add__(self,y):
        self.real = self.real + y.real
        self.imag = self.imag + y.imag
        return self
    def show_val(self):
        print(self.real,self.imag)


num1 = Algebra(2.5,6.5)
num2 = Algebra(3.5,4.99)
num3 = num1+num2
num3.show_val()


class Numeric_Str():
    def __init__(self,Str = ''):
        self.Str = Str
    def __int__(self):#operator overloading
        return int(self.Str)
num = Numeric_Str('1024')
print(num.Str)
print(int(num.Str)*2)


class SumPair():
    def __init__(self,lst):
        self.List = lst
        self.List_len = len(lst)
        self.i1 = 0
        self.i2 = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.i2 == self.List_len:
            raise StopIteration
        else:
            self.sum_pair = self.List[self.i1]+ self.List[self.i2]
            self.i1 += 1
            self.i2 += 1
            return self.sum_pair

l =SumPair([1,2,3,4,5,6])
print(l.List)
for i in l:
    print(i)
