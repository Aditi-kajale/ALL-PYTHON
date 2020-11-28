# eg-1 on exception handling
nos = [10,20,30]

try:
	print("Element @ position 3 is",nos[3])
except IndexError:
	print("Element @ position 3 is not accessible")

print("Processing of main() continues......")
