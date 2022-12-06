'''
Q1.Write a program to calculate the Amout in 3 years
if Principal is 35000 and Rate is 3.5%.
Tip: Create variables of p,t,r,si,amt for
Principal,Time,Rate,Simple Interest and Amount
respectively and use the following formula_

'''
p,t,r = 35000,3,3.5
si = (p*t*r)/100
amt = p + si
print("Amount is :",amt)
