# print 20 lines, each line of 60 dashes

for r in range(1,21):
	# print a line of 60 dashes
	for c in range(1,61):
		print("-",end="")

	print("Row no-",r)  # to confirm & move to next line
