'''Perform the following operations on the st set :

st = { 1, 2, 4, 6, 8, 9, 12, 16, 15}
Remove the all the odd numbers from the set

Add the even numbers needed in the set to make it a set of all even numbers less than 20 (except 20)

Print the set'''

st = { 1, 2, 4, 6, 8, 9, 12, 16, 15}
st.remove(1)
st.remove(9)
st.remove(15)
st.add(10)
st.add(14)
st.add(18)
print(st)