# To create a self initialised datetime object
from datetime import datetime

d,m,y = input("Enter the day, month & year :- ").split()
d = int(d)
m = int(m)
y = int(y)

# to create a date from above data, call the constructor of datetime class
dt = datetime(y,m,d)

print("Date accepted from user is",dt)

# breaking a date into day, month & year
# day, month & year are attributes of datetime object
dy = dt.day
mth = dt.month
yr = dt.year

print("Day is",dy,"month is",mth,"year is",yr)
