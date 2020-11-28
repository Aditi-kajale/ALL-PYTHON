# an eg of attributes of function objects - 1

def fn(no):
	return no * no

setattr(fn,"author","Shevade")
print("Author of fn() is",getattr(fn,"author"))
# to update/modify an attribute
setattr(fn,"author","Sandeep Shevade")
print("Author of fn() is",getattr(fn,"author"))
setattr(fn,"version",1.0)
print("Version of fn() is",getattr(fn,"version"))

# there is a built in attribute for every object called as _ _dict_ _ (dunder attribute)
# (these normally start & end with 2 underscores, so that we can avoid conflict between our
# attributes & the built in) which is a dictionary object & contains all the attributes & values
# defined for that object
print("Attributes of fn object are",fn.__dict__)

# checking the presence of an attribute
print("Does fn() have a version?",hasattr(fn,"version")) # True
delattr(fn,"version")
print("Does fn() have a version?",hasattr(fn,"version")) # False


