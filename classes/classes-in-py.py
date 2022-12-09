class Coder():
    #self is a variable denoting class Coder
    def __init__(self, name):
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
del(cd.language)
print(cd.language)