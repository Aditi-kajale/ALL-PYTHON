# Understanding the working principle/mechanism of different method types in Python i.e.
# instance, class & static methods
class MyClass:
	def inst_meth(self):
		print("Instance method called with parameter 'self' containing",self)

	@classmethod
	def cls_meth(cls):
		print("Class method called with parameter 'cls' containing",cls)

	@staticmethod
	def stat_meth():  # no implicit arg like above 2 methods
		print("Static method called with no parameters")

#main scope
obj = MyClass()
obj.inst_meth()
#optional way to call instance method
MyClass.inst_meth(obj)  # if called using class name, 1st parameter should be object of that
			# class

MyClass.cls_meth()  # here the class passes itself auto to the class method
#optional way to call class method
obj.cls_meth()

MyClass.stat_meth()
obj.stat_meth()
