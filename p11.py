# to accept the fullname & print only firstname & initials separately
fullname = input("Enter fullname:- ")

print("Your firstname is",fullname.split(" ")[0])
print("Your initials are",fullname.split(" ",1)[1])
