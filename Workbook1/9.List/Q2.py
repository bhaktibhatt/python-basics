'''
Q2.Create two lists namely
odd = [1,3,5,7,9]
eve = [2,4,6,8]
and perform the following actions_
• Combine the two lists in num list
• Add 10 to the list
• Report the total number of elements in the list
• Sort the list in descending order
• Remove all the elements in the list
'''
odd = [1,3,5,7,9]
eve = [2,4,6,8]
num = odd + eve
print(num)
num.append(10)
print(num)
print(len(num))
num.sort(reverse=True)
print(num)
num.clear()
print(num)