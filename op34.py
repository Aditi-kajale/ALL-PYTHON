# egs of map()
#eg - 1, write a function which returns the name & length of each item in a sequence
# if sequence is a list with names of fruits, then name & length of each fruit should be stored
# in the list e.g.  [('apple',5),('banana',6),('oranges',7),('lichi',5)]

def fn(item):
	return item, len(item)

l = ['apple','banana','oranges','lichi']

# to pass each item of list & get it's length, no need to use a loop. Instead use map()
l1 = list(map(fn,l)) # map() has 2 args, 1 function & 2 sequence

print(l1)

#eg - 2, Convert all the temp readings in deg F to deg C which are stored in a tuple
temp_f = 10,20,30,40,50    # csv are stored auto in tuple i.e. (10,20,30,40,50)
temp_c = tuple(map(lambda f : round((f-32)*5/9,2),temp_f))

print("Corresponding temps in deg C are",temp_c)

#eg - 3, To Add Elements of 2 lists & create a new list
l1 = [1,2,3,4,5]
l2 = [6,7,8,9]
# if lists to be added are of unequal length, then map() will stop when the shortest list is
# consumed

l = list(map(lambda x,y : x + y,l1,l2))

print("Added list is",l)

#eg - 4, Applying a bunch of functions or mapping a list of functions to map()
# To display the sin, cos & tan value for pi i.e. 3.14
from math import sin, cos, tan, pi

lst_fns = [sin,cos,tan]

l = list(map(lambda fn : fn(pi),lst_fns))

print("sin, cos & tan of pi is",l)




















