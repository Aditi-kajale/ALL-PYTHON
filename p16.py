""" 
Calculate the total bill amount of a customer of telephone company
by using the following rules
1) If no of calls <= 80, bill amount is Rs. 250/-
2) If no of calls > 80 but <= 160, then the cost is Rs 0.60 per call for calls>80
3) If no of calls > 160 but <= 250, then the cost is Rs. 0.50 per call for 
calls > 160
4) If calls exceed 250, then the cost is Rs. 0.40 per call
"""
no_calls = int(input("Enter the no of calls in a month :- "))

if no_calls <= 80:
	bill_amt = 250
elif no_calls in range(81,161):
	bill_amt = 250 + (no_calls-80) * 0.6
elif no_calls in range(161,251):
	bill_amt = 250 + 80 * 0.6 + (no_calls-160) * 0.5
else:
	bill_amt = 250 + 80 * 0.6 + 90 * 0.5 + (no_calls-250) * 0.4

bill_amt = round(bill_amt,2)
print("Bill Amount is Rs.",bill_amt)
