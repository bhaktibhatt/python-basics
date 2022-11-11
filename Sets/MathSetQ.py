'''Items that has discount are the followings :

ProductA, ProductC, ProductY, ProductX, ProductL
Items whose coupons you have are the followings :

ProductY, ProductM, ProductR, ProductC, ProductE
Print the list of names of the items that has discount and whose coupon you have'''

discount = {'ProductA', 'ProductC', 'ProductY', 'ProductX', 'ProductL'}
coupon = {'ProductY', 'ProductM', 'ProductR', 'ProductC', 'ProductE'}
print(discount & coupon)