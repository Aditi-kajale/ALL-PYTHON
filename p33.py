# to accept the days of the week & display the day/s with min temp 
# (coolest day/s)
daily_temps = {}   # dictionary

for i in range(7):
	day,temp = input("Enter the day & temp :- ").split(" ")
	temp = int(temp)
	daily_temps[day] = temp

# m = min(daily_temps.values())    # short cut, name of var should not be
			# that of a function

# goal is to find the min temp first
m = list(daily_temps.values())[0]

for key in daily_temps.keys():
	if m > daily_temps[key]:
		m = daily_temps[key]

# display all months and temps where temp = m
print("Days & temps are")
for key in daily_temps.keys():
	if m == daily_temps[key]:
		print(key," - ",daily_temps[key])






