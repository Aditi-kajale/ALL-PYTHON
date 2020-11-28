# To test the magical/dunder methods on int values

x,y = 5,2

print("Addition of 5 and 2 is",x.__add__(y))   # 7, + is binary operator, so we reqd 2 int object
print("Subtraction of 5 and 2 is",x.__sub__(y))   # 3
print("Multiplication of 5 and 2 is",x.__mul__(y))   # 10
print("True division of 5 and 2 is",x.__truediv__(y))   # 2.5
print("Floor division of 5 and 2 is",x.__floordiv__(y))   # 2
print("Is 5 greater than 2 is",x.__gt__(y))   # True
# no support for __iadd__() for int type in Python which in general is used to overload +=
# operator
x += y
print("Value of x is",x)