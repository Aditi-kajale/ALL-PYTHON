# alphabet pattern - 1

for r in range(1,6):
	ch = 'A'  # every row starts with letter 'A'
	for c in range(1,r+1):
		print(ch,end="")
		# ch += 1  # error, cannot concantenate int to str
		ch = chr(ord(ch) + 1)  # ord() returns ascii code of char and chr() returns char if ascii code is given

	print()

				