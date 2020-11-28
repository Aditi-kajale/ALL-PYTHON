# set comprehensions
# This is similar to list comprehension except that the set comprehension ensures that the
# output doesn't contain duplicate values. We can create a set comprehension using the
# syntax of list comprehension except that we use { } to define a set rather than [ ] used to
# define a list
# eg - 1, display the unique vowels in foll sentence
sent = "i was not feeling well yesterday"

s1 = {el for el in sent if el in 'aeiou'}  # fetch the char from sent only if it's a vowel

print("Unique vowels in sent are",s1)

"""
sort Vs sorted

1. sort is a method which is available only in list & string objects whereas sorted is a function
2. methods are called using object reference only where as functions receive object as it's parameter
3. methods normally affect the object's state which is not so with function
"""
print("Sorted Unique values are",sorted(s1))

#eg-2, display the count of each animal from foll list
l = ['dog','cat','dog','rat','cat','dog','rat','rat','dog']

s2 = {(el,l.count(el)) for el in l}
print("s2 contains",s2)
print("Animals with names in DESC order by their nos is",sorted(s2,key=lambda el : el[1],reverse=True))

