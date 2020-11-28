# an eg of numeric types
# as python is dynamically typed, var declaration not reqd
no = 2 ** 1000  # int can store any large no, limited to available memory
print("no = ",no)
# print no with , separator in '000
print("no = ",format(no,","))

print(type(no))  # class <int>

no = 5
print("square of no",no,"is",no*no)

# int literal
no = 123_456_789  # use _ for clarity
print(no)

# float - accuracy upto 15 decimals
pi = 22 / 7
print("pi = ",pi)  # prints all decimals
print("pi = %.3f" %pi)  # print 1st 3 decimals only
pi = 3.14_28_534   # _ should not preceed or follow . (dot)
print("pi = ",pi)

# complex nos
a = 3 + 2j
print("a contains",a)
print("real part in complex no a is",a.real)
print("imaginary part in complex no a is",a.imag)

b = 1 - 3j

print("Product of complex nos a and b is",a*b)
print(type(a))   # class <complex>


