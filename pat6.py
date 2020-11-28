# Diamond * Pattern

# Upper Triangle
for r in range(1,6):
	# Space Pattern
	for c in range(1,6-r):
		print(" ",end="")

	# Star Space Pattern
	for c in range(1,r+1):
		print("* ",end="")

	print()  

# Lower Triangle
for r in range(4,0,-1):
	# space pattern
	for c in range(1,5-r):
		print(" ",end="")

	# space star pattern
	for c in range(1,r+1):
		print(" *",end="")

	print()
