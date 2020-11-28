# accept a string from user & determine whether it is a palindrome or not
word = input("Enter a word:- ")
revword = word[::-1]   # step of -1 also tells the compiler to read the string
			# from end & proceed backwards
if word==revword:
	print("Given word",word,"and it's reverse",revword,"is same & hence palindrome")
else:
	print("Given word",word,"and it's reverse",revword,"is not same & hence not palindrome")
	