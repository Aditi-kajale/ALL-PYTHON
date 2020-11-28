# accept source and target filenames from user & copy the contents of source
# into target file. While copying, convert capital letters to small letters & vice versa.
# Also convert digits to digit 9 and special chars to char $ except space & ENTER
from os.path import exists
from sys import exit

src = input("Enter source filename :- ")
tgt = input("Enter target filename :- ")

if not exists(src):
	print("File",src,"doesn't exist")
	exit()

#create file objects
file_obj_src = open(src)
file_obj_tgt = open(tgt,"w")

# the file object is an iterable & hence we can use a loop to read each line from it
for line in file_obj_src:
	for ch in line:
		# get the ascii code of char read
		no = ord(ch)
		if no >= 65 and no <= 90:  # capital letter
			no += 32
		elif no >= 97 and no <= 122:   # small letter
			no -= 32
		elif no >= 48 and no <= 57:  # digit
			no = 57    # ascii code of 9
		elif ch == ' ':          # ascii code of space is 32
			pass
		elif ch == '\n':      # ascii code of ENTER is 13
			pass
		else:   # symbol
			no = ord('$')

		ch = chr(no)
		file_obj_tgt.write(ch)  # write the converted char to target file

file_obj_src.close()
file_obj_tgt.close()
print("File contents copied successfully after reqd conversions")

		











