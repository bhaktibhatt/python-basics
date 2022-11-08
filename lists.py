L1 = [90,45,23,"Python","Javascript","C"]
print(L1)
L1[-1] = "Java" 
print(L1)   
print(L1[3:])

odd = [1,3,5,7]
even = [2,4,6,8]
num = [odd,even]
num2 = odd+even
num3 = [*odd,*even]
print("List concatenate")
print(odd+even)
print(num)
print(num2)
print("list unpack")
print(num3)

print("List built in functions~")
print("\nSort-->")
num3.sort()
print(num3)
print("\nappend-->")
num3.append(9)
print(num3)
print("\ndeleting specific value-->")
num3.remove(2)
print(num3)
print("\npopping using index the index itself gets deleted-->")
num3.pop(7)
print(num3)
#print(num3[7])
print("\ndelete using del method will delete the value in the index")
#del(num3[8])
del(num3[4])
print(num3)

print("reversing list") 
num3.reverse()
print(num3)
print(num3.index(3))
print("count of a element")
num3.append(7)
print(num3)
print(num3.count(7))
#num3.clear() will clear the list
print(len(num3))
print(bool(5 in num3))