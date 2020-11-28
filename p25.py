# WAP to display the sum of all elements of a jagged list

l = [[1,2,3,4],[5,6],[7,8,9]]

sum = 0
"""
for i in range(len(l)):    # 3
	for j in range(len(l[i])):  # will differ from row to row
		sum += l[i][j]
"""

# for each loop (alternative technique)
for row in l:
	for col in row:
		sum += col

print("Sum of elements of list l is",sum)  # 45