'''Q1.Write a program that swaps the values of variables
a and b. I do not allow you to use a third
variable. You also may not perform arithmetic on a and b.
'''
def swap():
    a = int(input("enter a:"))
    b = int(input("Enter b:"))
    a,b = b,a
    print("Enter a:",a)
    print("Enter b:",b)
swap()

