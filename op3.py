# A program which makes use of functions kept in a different folder than this program)
from pyth_modules import our_functions

s = input("Enter a string :- ")
#nested fn call
print("String in upper case is",our_functions.make_caps(s))
print("String in lower case is",our_functions.make_small(s))
