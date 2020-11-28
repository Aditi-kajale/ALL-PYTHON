# Triangle * Pattern - Pascal Triangle

for r in range(1,6):
	# Space Pattern
	for c in range(1,6-r):
		print(" ",end="")

	# Star Pattern
	for c in range(1,r+1):
		print("* ",end="")

	print()  
