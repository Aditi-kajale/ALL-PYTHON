# to wish the user depending upon the time of the day
from datetime import datetime

#dt = datetime.now()
#hrs = dt.hour     # hour attribute returns the hours from current time

# shortcut
hrs = datetime.now().hour

print("Good Morning" if hrs < 12 else "Good Afternoon" if hrs < 17 else "Good Evening")

