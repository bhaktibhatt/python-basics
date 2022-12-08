'''Create a total variable which will store the total value done in shopping and a discount variable (with 0 value as starting) and in create a if statement where

if the total is over 500 give 5% of discount or if the promotional item is bought give 10% of discount or if the total is over 1000 give 10% of discount else no discount.

Calculate the total and print the total and discount% and discount value for the following total like

Discount : discount% OFF -discount
Total : total'''
total = 760
discount = 0
promo_item_bought = True

if total >= 500:
    if promo_item_bought:
        discount = 10

    else:
        discount = 5

elif total>=500 and promo_item_bought:
    discount = 10

elif total >= 1000:
    discount = 10

else:
    discount = 0


total_discounted = total - total*discount/100
print("Discount : {}% OFF -{}".format(discount, total*discount/100))
print("Total : {}".format(total_discounted))


