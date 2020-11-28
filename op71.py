#accept a source and target file names from user and copy the contents of source 
# into target
from os.path import exists
from sys import exit

src = input("Enter the filename to read :- ")
tgt = input("Enter the filename to write :- ")

if not exists(src):
	print("Source file",src,"doesn't exist")
	exit()

# create 2 file objects to operate the read() & write()
file_obj_src = open(src)
file_obj_tgt = open(tgt,"w")

file_obj_tgt.write(file_obj_src.read())  # write() accepts string which contains all the
				# contents of src file

file_obj_src.close()
file_obj_tgt.close()
print("File contents copied successfully")



