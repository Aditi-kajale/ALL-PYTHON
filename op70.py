# accept a filename from user & display it's contents
from os.path import exists  # exists is a function to check for existence of a file
import sys   # to access the exit()

fn = input("Enter the filename to read :- ")

#validation, rejection first
if not exists(fn):
	print("File",fn,"doesn't exist")
	sys.exit()  # if sys is not reqd, use    from sys import exit  @ top

file_obj = open(fn,"r")  # 2nd parameter is optional, bcoz default access mode is r

print("File contents are")
print(file_obj.read())

file_obj.close()





