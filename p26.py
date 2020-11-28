# accept m x n matrix of int values from user & display it alongwith row
# & column totals

m = int(input("Enter the no of rows :- "))
n = int(input("Enter the no of columns :- "))

l = []    # empty matrix/list

for i in range(m):
	row = []
	for j in range(n):
		no = int(input("Enter element " + str(i) + str(j) + ":- "))
		row.append(no)
	# now append the row to list
	l.append(row)


del row
#confirm & print row totals
for row in l:
	sumr = 0
	for col in row:
		print(col,end="\t")
		sumr += col  #get the term in total

	print(sumr)  # go to next line

#print column totals below each column
for i in range(n):
	sumc = 0
	for j in range(m):
		sumc += l[j][i]

	print(sumc,end="\t")






	