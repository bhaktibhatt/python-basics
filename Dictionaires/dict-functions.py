#<--Built-In functions in python-->
tpl1 = ('key1', 'key2', 'key3')
vals = (6)
dt = dict.fromkeys(tpl1,vals)
dt1 = dict.fromkeys(tpl1)
print(dt1)
dt1['key1'] = 1
dt1['key2'] = 2
dt1['key3'] = 3
print(dt1)
dt1.pop('key3')
print(dt1)
dt1.update({'key4':4})
print(dt1)
dt1.clear()
print(dt1)

dt2 ={'a1':1,'a1':2}
print(dt2)