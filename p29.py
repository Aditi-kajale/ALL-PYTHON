# remove the duplicates from given list

l = [0,-19,8,-19,7,5,6,0,0,6]

temp = []

for el in l:
	# check whether it is already present in temp
	if el not in temp:
		temp.append(el)

print("Before deleting duplicates, l was",l)
l = temp
del temp
print("After deleting duplicates, l was",l)
