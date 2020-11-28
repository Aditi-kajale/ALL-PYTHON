# an eg of set
# to accept names of 5 fruits & store them in a basket w/o duplicates

basket = set()

for i in range(5):
	fruit = input("Enter fruit name :- ")
	basket.add(fruit.lower())

print("Fruit basket contains",basket)

basket2 = ['banana','guava','orange','pineapple']

basket.update(basket2)

print("Now, Fruit basket contains",basket)
print("apple in basket?",'apple' in basket)
