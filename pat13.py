# Toran Pattern, Left to Right approach
nosp = 1
for r in range(6,0,-1):

	# LHS
	for c in range(1,r+1):
		print("*",end="")

	# space pattern
	# 6th row contains no space
	if r != 6:
		for c in range(1,nosp+1):
			print(" ",end="")

		nosp += 2

	# RHS
	for c in range(1,r+1):
		if r == 6 and c == 1:
			pass
		else:		
			print("*",end="")


	print()
