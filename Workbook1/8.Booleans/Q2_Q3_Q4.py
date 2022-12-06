'''
Q2.Write a program to generate 3 False values.
Q3.Write a program to generate 3 True Values.
Q4.Write a program using all the operators you learned in this lesson.
'''
print('\nQ2.')
n1,n2,n3,n4 = 1,2,3,4
print(bool(n1 == n2))
print(bool((n2+n1) != n3))
print(bool((n4%n2) == n1))
print("\nQ3.")
print(bool((n2+n1) == n3))
print(bool(n2))
print(bool(n4>n1))
print('\nQ4.')
print(n1+n2,'\n',bool(n2>n1),'\n',n4%2)