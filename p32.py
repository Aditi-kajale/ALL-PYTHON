# an eg of mathemetical operations on set
s1 = set('abhijit')
s2 = set('abhishek')

print("Characters in s1 not in s2 ? ", s1-s2)   # j, t
print("Characters in s1 not in s2 ? ", s1.difference(s2))

print("Characters common in s1 and s2 ? ", s1&s2)  # a, b, h, i
print("Characters common in s1 and s2 ? ", s1.intersection(s2))

print("Combined Characters in s1 and s2 ? ", s1|s2)  # a, b, h, i, j, t, s, e, k
print("Combined Characters in s1 and s2 ? ", s1.union(s2))

print("Other than common Characters in s1 and s2 ? ", s1^s2)  # j, t, s, e, k
print("Other than common Characters in s1 and s2 ? ", s1.symmetric_difference(s2))