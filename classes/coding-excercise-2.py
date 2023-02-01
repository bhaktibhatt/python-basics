'''
In a hotel, there are guests coming who may be registered or not.
You'll find the list of registered guests along with their keys in the registrations.txt (you can copy the same in your solution).

Create a Guest class and store the registrations in it.
While initializing, pass the guest name and store it as name.

Then create a method is_regd() to print 'Registered' or 'Not Registered' when the guest is registered or not respectively.

Create a method get_key() to print the key of the guest.

Create another method, reg() to register the guest and assign a key to that guest from the below list of Keys 
(same can be found in the registrations.txt)

kys = [ 'A010','A012','A014','BQ01']

Also, print a message 'Sorry, no vacant rooms available' if there are no keys or the kys list becomes empty (when registering).



After creating the Guest class, receive the following guests (i.e. create objects for them):

Josh

Hans

Evan

Kyle

Ted

Karl

Sam

For each guest, you've to

print the name of the guest,

their registration condition,

print the Key if registered else register and then print the key like

Guest1                 # guest name using print(guest.name)
Not registered         # Using the guest.is_regd()
Key : A000             # Using guest.get_key()

registrations = {
"John":"A011",
"Kyle":"A009",
"Jake":"BQ02",
"Tamra":"A015",
"Josh":"BQ03 ",
}

kys = [ 'A010','A012','A014','BQ01']
'''
registrations = {
"John":"A011",
"Kyle":"A009",
"Jake":"BQ02",
"Tamra":"A015",
"Josh":"BQ03",
}
kys = [ 'A010','A012','A014','BQ01']


class Guest():
    def __init__(self,name):
        self.name = name
    def is_regd(self):
        if self.name in registrations:
            print("Registered")
        else:
            print("Not Registered")
            Guest.reg(self)
    def reg(self):
        print('Registering Guest '+self.name)
        if len(kys)!= 0:
            registrations.__setitem__(self.name,kys.pop(0))
        else:
            print('Sorry, no vacant rooms available')
    def get_key(self):
        for key, value in registrations.items():
            if self.name == key:
                print("Key:"+value)

g1 = Guest('Josh')
print(g1.name)
g1.is_regd()
g1.get_key()


g2 = Guest('Hans')
print(g2.name)
g2.is_regd()
g2.get_key()



g3 = Guest('Evan')
print(g3.name)
g3.is_regd()
g3.get_key()



g4 = Guest('Kyle')
print(g4.name)
g4.is_regd()
g4.get_key()
print(kys)


g5 = Guest('Ted')
print(g5.name)
g5.is_regd()
g5.get_key()
print(kys)


g6 = Guest('Karl')
print(g6.name)
g6.is_regd()
g6.get_key()
print(kys)


g7 = Guest('Sam')
print(g7.name)
g7.is_regd()
g7.get_key()