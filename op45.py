# To prove that generator object can be paused & continued as & when reqd
g = (no for no in range(1,101))

#suppose these nos are record nos & we want to process them in 2 batches, each of 50 recs
for i in g:
	print("Record no",i,"processed")
	if i >= 50:
		break

print("\nSome other process to be carried out.......")

for i in g:
	print("Record no",i,"processed")
