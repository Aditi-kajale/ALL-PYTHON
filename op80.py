# an eg of a simple frame/window from TKinter
from tkinter import *  # Label, Button, Entry, ...... now the widgets can be referred
			# directly by their names

my_window = Tk()  # object of class Tk created with my_window
# setting the title & size by calling special methods of Tk object
my_window.title("My 1st GUI Appln")
#my_window.geometry("500x500")  # frame of size 500px x 500 px gets created
# if we need the frame @ a particular position
my_window.geometry("500x500+400+250")  # width,ht, left & top margins

my_window.option_add("*font","Arial 15 bold") # change the default font settings
				# for all widgets in frame

def display_result():
	# validation for empty Entry
	name = txtname.get()
	if name == "":
		txtname.insert(0,"Pls. enter your name")
		return  # terminate the function

	# update the lblresult with personal message
	lblresult.configure(text="Welcome " + name + " to TKinter GUI Appn")

# design the widgets and add them to Grid Geometry Manager
# this manager controls the layout of my_window/frame
# Grid Manager creates a table of rows & columns i.e. Matrix to accomodate
# widgets. The widgets are placed on the basis of row & col position using grid()

lbl = Label(my_window,text="Enter your name:- ", padx=20, pady=20) 
			 # 1st parameter to constructor
			# is root pane/parent window, 2nd is Caption
lbl.grid(row=0,column=0) # negotiates position

txtname = Entry(my_window)
txtname.grid(row=0,column=1)

btnclick=Button(my_window,text="Click Me",command=display_result,padx=10,pady=10) 
			# here parameter "command" (named/keyword arg) in
			# constructor will trigger the event on "click" of button
			# and call the function "display_result()"
btnclick.grid(row=1,column=0,columnspan=2) # merge 2 cols of row=1

lblresult = Label(my_window,text="Welcome To Databyte",pady=50)
lblresult.grid(row=2,column=0,columnspan=2)

# print(id(my_window),type(my_window))   # to verify python's role in this appn
my_window.mainloop()  # runs the GUI appn
