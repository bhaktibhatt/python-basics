'''
Q2.Create a list of random strings and create a
dictionary using the list as keys and the length of
the strings as its value.
'''
lst = ['Python', 'JS', 'Java', 'C']
dct = dict.fromkeys(lst)
dct['Python'] = len(lst[0])
dct['JS'] = len(lst[1])
dct['Java'] = len(lst[2])
dct['C'] = len(lst[3])
print(dct)
