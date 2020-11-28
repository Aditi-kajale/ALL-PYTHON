# Accept the extension of a file from user and display all files in current working
# directory with that extension and also their count
import os

extn = input("Enter the extension of file/s :- ")

files = os.listdir()  # this function returns a list object containing all the file
		# names from current working dir

count = 0

# list is an iterable type
for file in files:   # file is a string containing the filename
	if file.endswith(extn):
		print(file)
		count += 1

if count==0:
	print("No file/s found with extension",extn)
else:
	print("No of files are",count)


