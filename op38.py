# egs of list comprehensions i.e. creating new lists from scratch or using data of other lists
# which meet a certain condition

# eg - 1, create a new list of squares of nos from 1 - 10

"""
if list comprehension is not used
sq = [ ]  # blank list

for i in range(1,11):
	sq.append(i * i)

print("sq list contains",sq)
"""
sq = [i * i for i in range(1,11)]    # followed by  if i%2 != 0 (optional if we require only squares of
			# Odd nos from 1-10

print("sq list contains",sq)


#eg - 2, Combine the elements of 2 lists, only if they are unequal/not same

l1 = [1,2,3]
l2 = [3,1,4]

# expected result
# l = [(1,3),(1,4),(2,3),(2,1),(2,4),(3,1),(3,4)]

"""
long cut

l = [ ]
for el1 in l1:    # el1 represents each element of l1
	for el2 in l2:  # el2 represents each element of l2
		if el1 != el2:
			l.append((el1,el2))

print("Combined list is",l)
"""
l = [(el1,el2) for el1 in l1 for el2 in l2 if el1 != el2]
	
print("Combined list is",l)


#eg - 3, To compare data of 2 lists & add common elements only
l1 = ['eraser','pencil','sharpner','compass box']
l2 = ['ruler','pencil','marker','eraser']

#expected result
# l = ['eraser','pencil']

#l = [el1 for el1 in l1 for el2 in l2 if el1 == el2]  # OK but inefficient bcoz it is nested loop
l = [el1 for el1 in l1 if el1 in l2]  # More concise

print("Common elements are",l)

#eg - 4, To compare data of 2 lists l1 & l2 and add unique elements only i.e. eliminate duplicates
l = []

[l.append(el) for el in l1+l2 if el not in l] # earlier techniques fail bcoz in earlier techniques, every
			# time it looks in l, it is an empty list only. Hence we cannot
			# stop the addition of duplicate elements.
print("Unique elements from l1 & l2 are",l)



#eg - 5, To Create a Flattened list
l = [[1,2,3],[4,5],[6,7,8]]  #nested list i.e. 2D list

# expected result
# fl = [1,2,3,4,5,6,7,8]

"""
long cut
fl = [ ]  # empty list
for row in l:   # row is an actual list
	for col in row:  # col is actual element of list referred ie row (not index)
		fl.append(col)
"""

fl = [col for row in l for col in row]
print("Flattened list is",fl)


#eg - 6, Using list comprehension, create a list with values of constant PI with an accuracy
# of 1-5 decimals
#expected result
from math import pi

l = [round(pi,no_decimals) for no_decimals in range(1,6)]

print("Values of pi with decimals 1-5 are",l)

#eg-7, Calculate the price of items of a list after 5% tax on them

item_rates_before_tax = [10,20,30,40,50]

#eg-8, replace the given price list with given price if price > 2 else replace it with 0

item_prices = [1.25,2.25,3,1,0.9,10]







































