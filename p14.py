# Find the charges for sending a parcel by courier service. The charges are
# Rs. 30/- for 1st 1 KG & Rs. 10/- for 500 gm or less thereof
wt_kg =  float(input("Enter the wt of parcel in KG :- "))
wt_gm = wt_kg * 1000

if wt_gm <= 1000:
	charges = 30
else:
	if (wt_gm - 1000) % 500 == 0:
		charges = 30 + (wt_gm - 1000) // 500 * 10
	else:
		charges = 30 + ((wt_gm - 1000) // 500 + 1) * 10

print("The charges for sending a parcel weighing",wt_kg," KG is Rs.",charges)
