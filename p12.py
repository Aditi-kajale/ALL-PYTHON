# to accept the temperature in deg Farenheit or Celsius & convert it

#temp_type = input("Enter F/f for farenheit OR C/c for Celsius :- ")

print("Enter F/f for farenheit OR C/c for Celsius :- ",end="")
temp_type = input()

temp = float(input("Enter the temperature :- "))  # typecast str to float

if temp_type == 'F' or temp_type == 'f':
	conv_temp = (temp - 32) * 5/9
	#print(temp,"in deg F is",conv_temp,"in deg C")
	# to restrict the decimals, use str.format()
	print("{0} in deg F is {1:.2f} in deg C".format(temp,conv_temp))
else:
	conv_temp = 9/5 * temp + 32
	print("{0} in deg C is {1:.2f} in deg F".format(temp,conv_temp))
