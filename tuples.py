
tpl1 = (5,4,7,3,8,2 )
#tpl1[4] = 4 with give TypeError as tuple object does not support item assignment
#del(tpl)
#round bout way:
lst1 = list(tpl1)
lst1[0] = 10
tpl = tuple(lst1)
print(tpl)


#del(tpl[2]) not possible
#deleting and adding vals can be done by converting the tuple object to string object
#tuples are immutable cant be changed
tp2=(0,1,3,'b','h','k','t','i')
tp3 = tuple("Bhakti Bhatt")
lst = list("Bhakti")

print(tpl1)
print(tp2)
print(tp3)
print(lst)


t1 = ("python",)
print(t1)
print(type(t1))

print(tp3.index('a'))
print(tp3.count('h'))

print(sorted(tpl1))
print(tuple(sorted(tpl1)))
print(len(tpl1))
print(max(tpl1))
print(min(tpl1))