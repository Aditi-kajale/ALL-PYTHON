# eg-2 on exception handling with finally
import sys

nos = [10,20,30]

try:
	print("Element @ position 3 is",nos[3])
except IndexError:
	print("Element @ position 3 is not accessible")
	sys.exit()   # terminating the prog
finally:
	print("Code from finally executes always....")

print("Processing of main() continues......")
