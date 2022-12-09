'''In a hotel, there are guests coming with following registrations :

Name - John
Key - A011
Name - Kyle
Key - A009
Name - Jake
Key - BQ02
Name -  Tamra
Key  - A015
Name - Josh
Key - BQ13 
Create a function get_key() in which the name of a guest is passed as argument and 
the Key is printed if the guest is registered  like

#Sample Output
Key : BQ02

or Not Registered message is printed if the guest isn't registered

#Sample Output
Not Registered

The following guests have came :'''

guest_1 = 'Jake'
guest_2 = 'Tamra'
guest_3 = 'Ted'

reg_dic = {'John':'A011', 'Kyle':'A009', 'Jake':'BQ02', 'Tamra':'A015', 'Josh':'BQ13'}

def get_key(name):
    if name in reg_dic:
        print('Key : '+str(reg_dic.get(name)))
    else:
        print('Not Registered')

get_key(guest_1)
get_key(guest_2)
get_key(guest_3)
