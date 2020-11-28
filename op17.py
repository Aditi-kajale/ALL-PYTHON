#An eg of default arguments of a function
# We can provide default values to a function arguments. Once we provide a default value to a 
# function argument, that argument becomes optional during function call. If value for argument is
# not passed during function call, the default value is used by the function. However if the value is
# passed during function call, then the default value is ignored/overwritten
def info(name,course="Engineering",age=21):
	print(name,"completed",course,"@ the age of",age)

info("kamlesh")
info("mahesh",age=22)
info("sunita",course="mca",age=24)
info("ashok",course="bca")
#info("manish",course="bca",22) # SyntaxError, positional arg follows keyword arg

#Note - It is possible to specify default values for all args of a function. However the args with default
#values should be the trailing args only i.e. we cannot provide default values to args in random
#fashion. In other words, if we specify a default value for any arg of a function, then all args to it's
#right should be specified default values
