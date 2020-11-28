# an eg of while....else loop
# to check whether a value/item exists in a sequence like list or not &
# if it exists, returns it's position in list

basket = ['apple','banana','orange','strawberry']
fruit = input('Enter the fruit name :- ')

#print('Fruit',fruit,'exists in basket?',fruit in basket)

i = 0
while i < len(basket):
	if fruit == basket[i]:
		print('Fruit',fruit,'found @ pos',i+1)
		break    # terminate the search
	else:
		i += 1
else:
	print('Fruit',fruit,'not available in basket')

		