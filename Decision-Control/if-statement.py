num1 = 20
num2 = 90
if num1 != num2:
    print("Num1 is not equal to num2") 

tot = 600
bought_sale = True
dis = 0
# if tot >= 1000 or bought_sale:
#     dis = 10
#to just check condition in if we use pass keyword
#using else keyword
if tot >= 1000:
    dis = 10
else:
    dis = 0

total = tot - tot*dis/100
print(tot*dis/100)
print('Total is ',total)

#using eilf statement
name = 'Bhakti'
age = 17
status = 'Minor'
if age >= 65:
    status = 'Senior Citizen'

elif age >= 18 and age<= 64:
    status = 'Adult'

print(status)

Str = 'it\'s python'

if 'p' in Str:
    Str = 'It\'s Python'

elif 'i' in Str:
    Str.capitalize()

print(Str)


lst = ['Python','C', 'C++', 'Java']
print(lst)
if 'Python' not in lst: #if python is not in list i.e the condition is true the other elif block is not executed
    lst.append('Python')

elif 'Java' not in lst:
    lst.append('Java')

else: #this block will execute only if if elifs condition are false
    lst.append('Javascript')

print(lst)