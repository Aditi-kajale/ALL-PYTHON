# an eg of methods of list object

my_book = [123,"Basic Python","Guido Van Rossum",655.75]

#method-1
print("my_book contains",my_book)

#method-2
# to avoid printing [ ] & access every element individually
print("my_book contains ",end="")

# use for each loop
for el in my_book:
	print(el,end=" ")

#method-3
print("\nmy_book contains ",end="")
for i in range(len(my_book)):
	print(my_book[i],end=" ")

# to insert an item in list
my_book.insert(2,"Tata Publications")

print("\nAfter insert(), my_book contains",my_book)

# add no_pgs @ end of list
my_book.append(250)
print("After append(), my_book contains",my_book)

# update the author name
my_book[3] = 'G. V. Rossum'
print("After update, my_book contains",my_book)

# delete the item publisher
my_book.remove("Tata Publications")  # will raise ValueError if item is not
				# available

print("After remove(), my_book contains",my_book)



