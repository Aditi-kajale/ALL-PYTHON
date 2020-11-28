# egs of filter()
#eg-1, Display a list of adults from given list of persons & their age
# for a person to be qualified as an adult, his/her age >= 18 years
persons = [['paresh',25],['beena',15],['nita',19],['amit',18],['sunil',10],['kamlesh',35]]  # nested list

adults = list(filter(lambda person : person[1] >= 18,persons)) # return type of result is now a list
# "person" is an element of nested list "persons"
# person[0] ==> name, person[1] ==> age

print("Adults from persons list are",adults)


# eg-2, filter & display the odd nos from given fibonacci series
fibo_series = [0,1,1,2,3,5,8,13,21,34,55,89]

#long cut
#odd_nos = filter(lambda fibo_no : fibo_no % 2 != 0,fibo_series)

#print("Odd nos from fibo_series are",odd_nos) # prints the adr of object in memory

#for el in odd_nos:
#	print(el,end="  ")

# short cut
odd_nos = list(filter(lambda fibo_no : fibo_no % 2 != 0,fibo_series))
print("Odd nos from fibo_series are",odd_nos) # print the elements of the list
