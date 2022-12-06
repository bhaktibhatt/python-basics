'''Q3.Create a program to create a dictinary
dt = {'A':65,' B': 66,' C':67}
update the dictionary with the following dict
dtl = {'E':68,'F':69}
set the values of 'E' key to 69 and 'F' to 70.
'''

dt = {'A':65,' B': 66,' C':67}

dtl = {'E':68,'F':69}

dt.update(dtl)
print(dt)