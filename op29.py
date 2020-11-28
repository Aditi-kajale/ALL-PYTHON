# Application - 1 of decorator fn
# Write a decorator fn to check whether the no passed to a fn is a +ve non zero int
def chkno(func):   # decorator fn
	def validate(no):  # wrapper fn
		# check the no before passing it to calc_fv() or any other fn
		# in validations, always start with rejection
		if no <= 0 or type(no) != int:
			print("Pls enter a +ve non zero int value only")
			return  # terminate the fn

		print("Factorial value of",no,"is",calc_fv(no))

	return validate

#@chkno # short cut
def calc_fv(no):
	if no == 1:
		return 1

	return no * calc_fv(no-1)  # fv(no) = no * factorial value of it's previous no


#long cut
ref_validate = chkno(calc_fv)
ref_validate(8)  # displays the factorial value of 8
ref_validate(-8) # displays the error message
ref_validate(8.35) # --- do ---


