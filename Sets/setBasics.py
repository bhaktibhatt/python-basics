set1 = {1,2,0,3,3,3,3,3}
print("set1",set1)
set2 = set([1,2,3,3,5,3,'Bhakti',1,4,56,45])
set3 = {2,3,6,8,9}
#set4 = {set1,set2} TypeError: unhashable type: 'set'
#sets dont have indexing so they get printed unordered 
print("set2",set2)
#print(set4)
#set1[0] TypeError: 'set' object is not subscriptable
#QRemove the duplicates in the lst list and print it
#lst = [ 0, 12, 3 ,4 ,12, 4, 12, 34, 12, 33, 7, 8 , 2, 90, 23, 45, 12, 33]
lst = set([ 0, 12, 3 ,4 ,12, 4, 12, 34, 12, 33, 7, 8 , 2, 90, 23, 45, 12, 33])
print(list(lst))

s1,s2 = {0,1,2,3}, {4,5,6,7}
print(s1,s2)
s1.add(4)
print(s1)
s1.remove(0)
# s1.remove(10) KeyError: 10
s1.discard(10)#checks if 10 is present if yes then discards it
print(s1)
s1.discard(3)
print(s1)
s1.clear()
print(s1)
s1.update(s2)
print(s1,s2)
