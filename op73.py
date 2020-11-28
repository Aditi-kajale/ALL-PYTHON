# accept a filename from user & display it's contents in reverse order
import os
import sys


fn = input("Enter the filename :- ")

# validation
if not os.path.exists(fn):   # full qualifier
	print("Filename",fn,"doesn't exist")
	sys.exit()


file_obj = open(fn)  # the 2nd parameter is by default "r" i.e. read mode

# by default, the file pointer/cursor is @ the begining of file (read mode)
# (in append mode, it is @ end of file)
# bring the pointer to end of file, so that we come to know the no of chars in file
file_obj.seek(0,os.SEEK_END)
no_chars = file_obj.tell()   # for no_chars, base is 1, for position base 0
pos = no_chars - 1 # position of last char

while (pos >= 0):
	file_obj.seek(pos,os.SEEK_SET)
	ch = file_obj.read(1) # fetch only the current char where file pointer is
				# positioned
	print(ch,end="")
	pos -= 1

file_obj.close()










