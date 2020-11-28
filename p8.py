# an eg of keyword args in string.format()

print("I belong to {city} and in state of {state}".format(state='Maharashtra',city='Pune'))  # here order in format() doesn't matter

name = 'Ashish'
state = "Maharashtra"

print("I belong to {city} and in state of {st} and my name is {0}".format(name,city='Pune',st=state))  # positional args should preceed keyword
				# args

