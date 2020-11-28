# an eg of zip()
# eg - 1 of zip() using a couple of Strings to be mapped
s1 = 'pranjal'
s2 = 'rohit'
s3 = 'rohankumar'

s = list(zip(s1,s2,s3))  # zip() will stop when it reaches the end of smallest string i.e. rohit

print("s contains",s)

# eg - 2 of zip() to create a dictionary from a list & a tuple
# However here the zip() will accept only 2 iterables as it's parameters bcoz the dictionary
# contains key/value pairs
items = ['apple','banana','orange','strawberry']  # list
cost = 25,3,5,1  # tuple

d = dict(zip(items,cost))

print("d contains",d)

# eg - 3, to "unzip" the items of a zipped object, we can use the same function
z = zip(items,cost)
i,c = zip(*z)  # * operator will unzip/unpack the zipped object & return data in form of a tuple

print("Item names are",i)
print("Cost of items are",c)


