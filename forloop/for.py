lst = ['python', 'c', 'java', 12, 'JavaScript']
for i in lst:
    if i == 'JavaScript':
        print(i)
        continue
    if i == 12:
        break
    print(i.capitalize())

print(range(4))
print(list(range(5)))
print(list(range(2,5)))

for num in range(2,5):
    print(num)
    print('Bhakti')

#nested for loop
for n in [1,2,3]:
    for m in [1,2,3]:
        print(n,m)

print('test')
for i in range(5,0,-1):
    print(i)