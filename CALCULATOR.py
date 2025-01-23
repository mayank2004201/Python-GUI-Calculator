from tkinter import *

# Initialize the main application window
root = Tk()
root.title("My First GUI")

# Create an entry widget for user input
e = Entry(root, width=35, borderwidth=7)
e.grid(row=0, column=0, columnspan=4)

def button(number):
    # Insert the number at the end of the entry widget whenever a button is clicked
    e.insert(END, number)

# Explanation of button creation without parameters
# To create a button without passing parameters directly in the command,
# use the following format: button_name(root, ---, command=function_name)

# To pass parameter values from a button to a function, use:
# button_name(root, command=lambda: function_name(parameter_value))

# The following buttons will pass their respective values to the function when clicked
a1 = Button(root, text="1", padx=20, pady=20, command=lambda: button(1))
a1.grid(row=3, column=0)

a2 = Button(root, text="2", padx=20, pady=20, command=lambda: button(2))
a2.grid(row=3, column=1)

a3 = Button(root, text="3", padx=20, pady=20, command=lambda: button(3))
a3.grid(row=3, column=2)

a4 = Button(root, text="4", padx=20, pady=20, command=lambda: button(4))
a4.grid(row=2, column=0)

a5 = Button(root, text="5", padx=20, pady=20, command=lambda: button(5))
a5.grid(row=2, column=1)

a6 = Button(root, text="6", padx=20, pady=20, command=lambda: button(6))
a6.grid(row=2, column=2)

a7 = Button(root, text="7", padx=20, pady=20, command=lambda: button(7))
a7.grid(row=1, column=0)

a8 = Button(root, text="8", padx=20, pady=20, command=lambda: button(8))
a8.grid(row=1, column=1)

a9 = Button(root, text="9", padx=20, pady=20, command=lambda: button(9))
a9.grid(row=1, column=2)

a0 = Button(root, text="0", padx=75, pady=20, command=lambda: button(0))
a0.grid(row=4,columnspan=3)

# Function to clear the input field
def clear():
    e.delete(0, END)

# Store the first number entered by the user in the input field using e.get()
# Global variables f_num and math are used to maintain state across functions 
# f_num is set to the integer value of first_num after clearing the input field
def add():
    first_num = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_num)
    e.delete(0, END)

def subtract():
    first_num = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_num)
    e.delete(0, END)
        
def multiply():
    first_num = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_num)
    e.delete(0, END)
        
def divide():
    first_num = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_num)
    e.delete(0, END)

def power():
    first_num = e.get()
    global f_num
    global math
    math = "power"
    f_num = int(first_num)
    e.delete(0, END)

# Perform the arithmetic operation based on the selected operation and display the result
def equal():
    second_num = e.get()
    e.delete(0, END)
    
    if math == "addition":
        e.insert(0,f_num + int(second_num))
        
    if math == "subtraction":
        e.insert(0,f_num - int(second_num))
        
    if math == "multiplication":
        e.insert(0,f_num * int(second_num))
        
    if math == "division":
        e.insert(0,f_num / int(second_num))
        
    if math == "power":
        e.insert(0,f_num ** int(second_num))

# Create buttons for operations and layout them in the grid
b1 = Button(root,text="+",padx=20,pady=50,command=add)
b1.grid(row=3,rowspan=2,column=3)

b2 = Button(root,text="=",padx=20,pady=20,command=equal)
b2.grid(row=2,column=3)

b3 = Button(root,text="Clr",padx=20,pady=20,command=clear)
b3.grid(row=1,column=3)

b4 = Button(root,text="-",padx=20,pady=20,command=subtract)
b4.grid(row=1,column=4)

b5 = Button(root,text="*",padx=20,pady=20,command=multiply)
b5.grid(row=2,column=4)

b6 = Button(root,text="/",padx=20,pady=20,command=divide)
b6.grid(row=3,column=4)

b7 = Button(root,text="^",padx=20,pady=20,command=power)
b7.grid(row=4,column=4)

# Change button color on hover (currently not functional for all buttons)
def on_enter(event):
    button.config(bg='lightblue')

button.bind("<Enter>", on_enter)

# Start the main event loop for the application
root.mainloop()
