# alphabet pattern 2
ch = 'A'

for r in range(5,0,-1):
	temp = ch
	# space pattern
	for c in range(1,6-r):
		print(" ",end="")

	# char pattern
	for c in range(1,r+1):
		print(temp,end="")
		temp = chr(ord(temp) + 1)

	ch = chr(ord(ch) + 1)
	print()

