# an eg of positional arguments of string.format()

print("Learning {0} is {1} and {2}".format('Python','Fun','Simple'))

name = 'Ashish'
salary = 10000

print("My name is {0} and salary is {1}".format(name,salary))
# suppose we want comma for values in '000 & decimals
print("My name is {0} and salary is {1:,.2f}".format(name,salary))

item_code = 121
price = 14500.547

print("Item code is {0:05} and price is Rs. {1:,.0f}".format(item_code,price))
# in 1st place holder 0 is positional arg, 0-fill char, 5-total length of item_code