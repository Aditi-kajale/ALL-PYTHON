dfr# an eg of String indexing & slicing

name = "databyte"

# for indexing & slicing, base is 0 whereas for length, base is 1
print("0th char in name is",name[0])
# print("Last char in name is",name[len(name)]) # error, Index Error
print("Last char in name is",name[len(name)-1])

# slicing operation
# syntax for slicing is start,stop-1,step (default 1)
print("0th - 2nd char is",name[0:3])   # returns a substring from pos 0 to 2
print("Alternate chars in name are",name[0:len(name):2])  # dtbt

# if start & stop are not mentioned, default for start is 0 & stop is len()-1
print("Alternate chars in name are",name[::2])  # dtbt
print("All chars in given string are",name[:])  #databyte

# we can fetch chars from string from RHS also
print("From 0th to 2nd last char in name are",name[0:-2]) # databy





 