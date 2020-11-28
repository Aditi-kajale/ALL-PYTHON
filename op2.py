# an eg of a python module/script which makes use/calls functions of another module
import my_functions

no = int(input("Enter any no :- "))
print("Abs value of given no is",my_functions.abs(no))  #full qualifier for a fn call

from my_functions import abs, pow   # optional 1 or more....

print("Abs value of given no is",abs(no))  #full qualifier not reqd for a fn call

