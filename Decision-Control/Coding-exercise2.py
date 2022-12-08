'''Create a total variable which will store the total value done in shopping and a discount variable (with 0 value as starting) and create a if statement where

if the total is over 500 give 5% of discount or if the total is over 1000 give 10% of discount else no discount.

Calculate the total and print the total and discount% and discount value for the following total like (mind the spaces)

Discount : discount% OFF -discount
Total : total
'''
total = 870
discount = 0

if total >= 500 and total <= 1000:
    discount = 5

elif total >= 1000:
    discount = 10

else:
    discount = 0

total_discounted = total - total*discount/100

print('Discount : {}% OFF -{}'.format(discount,total*discount/100))
print('Total : {}'.format(total_discounted))

