'''
Create a class LenVal which will store the length of any data passed and a sho_val() method or 
function inside the LenVal class to print the length.
Create three objects of the class with the following values and use the sho_val() method on them

'Head'
[ 1, 9, 4, 2, 6]
(1, )
'''
class LenVal():
    def __init__(self,data):
        self.data = data
    def sho_val(self):
        print(len(self.data))

l1 = LenVal('Head')
l1.sho_val()
l2 = LenVal([ 1, 9, 4, 2, 6])
l2.sho_val()
l3 = LenVal((1, ))
l3.sho_val()