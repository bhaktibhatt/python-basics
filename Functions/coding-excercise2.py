'''Create a str_rev() function to print a reversed version of a string passed to the function as argument like,

'Word'  : 'Dorw'
Note that the output is capitalized and the last letter which may be upper or lower should be lower and also note it's format Word : Reversed

Perform the function on the following strings '''

Str1 = 'Desserts'
Str2 = "Live" 
Str3 = 'Pals'
Str4 = 'God'
Str5 = 'Raw'
def str_rev(n):
    Str = ""
    for i in n.lower():
        Str = i + Str
    return Str.capitalize()

print('{} : {}'.format(Str1, str_rev(Str1)))
print('{} : {}'.format(Str2,str_rev(Str2)))
print('{} : {}'.format(Str3,str_rev(Str3)))
print('{} : {}'.format(Str4,str_rev(Str4)))
print('{} : {}'.format(Str5,str_rev(Str5)))


