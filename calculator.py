# A simple calculator
# Author Ajith
from tkinter import *

# Generate the window
root = Tk()
root.title("")

# To make the window not resizable
root.resizable(0,0)

# Starting the window
cal=Label(root,text="Calculator")
cal.grid(row=0,columnspan=8)

# Required variables
variable=""
output_variable=StringVar()

# To show the output
calculation=Entry(root,textvariable=output_variable)
calculation.grid(row=2,columnspan=8)
calculation.focus()

# Functions for performing calculations
def calcs(input):
	try:
		global variable
		variable=variable+str(input)
		output_variable.set(variable)
	except:
		output_variable.set("Error")

def clear():
	try:
		global variable
		variable=""
		output_variable.set("")
	except:
		output_variable.set("Error")

def equals():
	try:
		global variable
		output=str(eval(variable))
		output_variable.set(output)
		variable=""
	except:
		output_variable.set("Error")

# Generating Buttons
Button0 = Button(root, text="0", command=lambda:calcs(0))
Button0.grid(row = 6, column = 2, padx=7, pady=7)

Button1 = Button(root, text="1", command=lambda:calcs(1))
Button1.grid(row = 3, column = 1, padx=7, pady=7)

Button2 = Button(root, text="2", command=lambda:calcs(2))
Button2.grid(row = 3, column = 2, padx=7, pady=7)

Button3 = Button(root, text="3", command=lambda:calcs(3))
Button3.grid(row = 3, column = 3, padx=7, pady=7)

Button4 = Button(root, text="4", command=lambda:calcs(4))
Button4.grid(row = 4, column = 1, padx=7, pady=7)

Button5 = Button(root, text="5", command=lambda:calcs(5))
Button5.grid(row = 4, column = 2, padx=7, pady=7)

Button6 = Button(root, text="6", command=lambda:calcs(6))
Button6.grid(row = 4, column = 3, padx=7, pady=7)

Button7 = Button(root, text="7", command=lambda:calcs(7))
Button7.grid(row = 5, column = 1, padx=7, pady=7)

Button8 = Button(root, text="8", command = lambda:calcs(8))
Button8.grid(row = 5, column = 2, padx=7, pady=7)

Button9 = Button(root, text="9", command=lambda:calcs(9))
Button9.grid(row = 5, column = 3, padx=7, pady=7)

Plus = Button(root, text="+", command=lambda:calcs("+"))
Plus.grid(row = 3, column = 4, padx=7, pady=7)

Minus = Button(root, text="-", command=lambda:calcs("-"))
Minus.grid(row = 4, column = 4, padx=7, pady=7)

Multiply = Button(root, text="*", command=lambda:calcs("*"))
Multiply.grid(row = 5, column = 4, padx=7, pady=7)

Divide = Button(root, text="/", command=lambda:calcs("/"))
Divide.grid(row = 6, column = 4, padx=7, pady=7)

Equal = Button(root, text="=", command=equals)
Equal.grid(row=6, column=3, padx=7, pady=7)

Clear = Button(root, text="C", command=clear)
Clear.grid(row = 6, column = 1, padx=7, pady=7)

Authorship=Label(root,text="Created by : Ajith")
Authorship.grid(row="7",columnspan=8)

# For making the window active
mainloop()
