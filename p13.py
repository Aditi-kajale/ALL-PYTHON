# egs on shorthand if

# print some statements for a condition
no = 10   # can be int or float value

print("no is +ve" if no > 0 else "no is -ve" if no < 0 else "no is 0")

# assignment for a condition  - eg 1
no = 0
abs_no = no if no > 0 else -no
print("Absolute value of",no,"is",abs_no)

# assignment for a condition  - eg 2
# print max no
a = 10
b = 15
c = -30
max = a if a > b and a > c else b if b > c else c
print("Max no is",max)
