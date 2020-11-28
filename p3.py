# an eg of boolean type (bool)

print("Is 10 > 5 ?",10>5)  # True
print("Is 10 < 5 ?",10<5)   # False
print(type(True))  # class bool
print(type(False))  # class bool
# print(type(true))  # error, name true not defined

true = 123
print(type(true))  # class <int>
print(type('true'))  # class <str>

# boolean arithmetic
# all values i.e. int or floats are treated as True & only 0 is False
print(bool(1)) # True
print(bool(-5.78)) # True
print(bool(0)) # False

print(True+7)  # 8
print(False - 7)  # -7
print(True + False)  # 1

# boolean expression
A = True
B = False

print(A and B)  # False
print(A or B)   # True
print(not A)   # False
print(not B)  # True
print(A == B)  # False
print(A != B)  # True

# compound boolean expressions, priority 1. not 2. and 3. or
C = False
print(A and B or C)  # False
print(A and (B or C))  # False
print(A or (B and C)) # True




