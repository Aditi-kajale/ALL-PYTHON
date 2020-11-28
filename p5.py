# exploring print()
print("Hello")
print("Sir")

# This will print the 2 words on 2 different lines bcoz the print() contains
# a default "end" keyword argument with value \n. Hence to print in single
# line, replace \n with a space
print("Hello",end=" ")
print("Sir")

day = 26
month = 1
year = 2020

print("Tomorrow is republic day i.e. date is ",end="")
print(day,month,year,sep="-")  # default separator is space
