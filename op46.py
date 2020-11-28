# an eg of self arg in a method of a class

class A:
	# meth defn
	def meth(self):   # write self here. The name "self" can be replaced by any name,
			# say "this", "x", ..... But conventionally/traditionally, it is 
			# called as "self"
		print("Hello")


# create an objct of class A
obj = A()
obj.meth()    # self is passed auto
# alternative tech, not used much
A.meth(obj) # Here obj refers to itself & hence called as "self"

