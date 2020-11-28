# an eg of radio buttons, layout created using Pack Geometry Manager
from tkinter import *

my_window = Tk()
my_window.title("An eg of radio buttons")
my_window.geometry("375x150+400+250")
my_window.option_add("*font","arial 14")  # plain text
my_window.configure(background="light green") 

my_window.option_add("*background","light green")
my_window.option_add("*foreground","red")


lblresult=Label(my_window,text="Favourite Programming Language",fg="blue")
lblresult.pack()

# here the output is based on selection of 1 of the 3 radio buttons
# So here TKinter provides us with "control variables" which will get updated whenever
# an event related to the control/widget takes place
radio_var = StringVar()  # These vars are created by calling the constructors of special
			# classes, eg IntVar(), DoubleVar()
# set the default value for radio_var
radio_var.set(" ") # No radio button is selected initially

def print_selection():
	lblresult.configure(text="Your Favourite language is " + radio_var.get())

r1=Radiobutton(my_window,text="C",variable=radio_var,value="C", command=print_selection)

r2=Radiobutton(my_window,text="CPP",variable=radio_var,value="C++", command=print_selection)

r3=Radiobutton(my_window,text="Java",variable=radio_var,value="Core Java", command=print_selection)

r1.pack(anchor=W)  # W - west (left), E - east (right) - are constants
r2.pack(anchor='w') # if constants are written in lower case, then use 'w'
r3.pack(anchor=W)

my_window.mainloop()
