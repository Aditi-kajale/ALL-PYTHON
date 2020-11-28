# numeric pattern, approach - line by line

no = 1

for r in range(1,6):
	if r == 1:
		for c in range(1,6):
			print(no,end="")
			no += 1
	elif r in [2,3,4]:
		print(r," ",6-r,end="")
	else:
		for c in range(5,0,-1):
			print(c,end="")

	print()
