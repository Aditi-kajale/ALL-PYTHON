# eg1 to print the data of variables
name = "Ashish"
salary = 10000

print("My name is",name,"and salary is",salary)
# using place holders & formatted string concept
print(f"My name is {name} and salary is {salary}")  # { } place holders for vars
# the drawback of above techniques is that we cannot change the
# format of data especially nos
print("My name is %s and salary is %.2f" % (name,salary))  # using format
			# specifiers like C lang - Old Python

# concept of raw string
path1 = "d:\\new\\test.txt"  # \ is escape sequence char
path2 = r"d:\new\test.txt"  # r - raw string wherein \ is not treated as a 
			#command but a plain char

print("path1 is",path1)
print("path2 is",path2)


