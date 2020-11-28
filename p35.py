# working with date & time
from datetime import datetime

dt = datetime.now()   # returns the current date & time of the system

print("Current date & time is",dt)

print("Abbreviated day of the week is",dt.strftime("%a"))   # Sun
print("Complete day of the week is",dt.strftime("%A"))   # Sunday
print("Complete day of the week in caps is",dt.strftime("%A").upper())   # SUNDAY

print("Abbreviated month name of the year is",dt.strftime("%b")) # Mar
print("Complete month name of the year is",dt.strftime("%B")) # March

print("Day of the month is",dt.strftime("%d"))   # 15
print("Month of the year is",dt.strftime("%m"))   # 03
print("Year without century is",dt.strftime("%y"))   # 20
print("Year with century is",dt.strftime("%Y"))   # 2020

print("Hours in 24 hour format are",dt.strftime("%H"))  # 10
print("Minutes from time are",dt.strftime("%M"))  # 15
print("Seconds from time are",dt.strftime("%S"))  # 35


