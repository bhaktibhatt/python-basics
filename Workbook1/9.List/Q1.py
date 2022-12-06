'''
QI.Create a list lang of 5 names
lang = ['C','C++','Java','Python','Js']
and perform the following actions_
• Insert 'Ruby' in the list
• Delete 'C' from the list'
• Replace 'Js' with 'JavaScript'
• Sort all the elements in the list
• Print the sorted list
'''
lang = ['C','C++','Java','Python','Js']
print(lang)
lang.append('Ruby')
print(lang)
lang.remove('C')
print(lang)
lang[3] = 'Javascript'
print(lang)
lang.sort()
print(lang)