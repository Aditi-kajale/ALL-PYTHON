# accept the month no from user & display the no. of days in that month
month = int(input("Enter the month :- "))

# validation, rejection first
if month < 1 or month > 12:
	print("Invalid Month")
elif month in [1,3,5,7,8,10,12]:  # member ship operator
	print("No of days are 31")
elif month in [4,6,9,11]:
	print("No of days are 30")
else:  # feb
	# 1st ask the user the year
	year = int(input("Enter the year :- "))
	if (year%4==0 and year%100!=0) or year%400==0:
		print("No of days are 29")
	else:
		print("No of days are 28")

