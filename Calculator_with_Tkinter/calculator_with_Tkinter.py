# importing tkinter package
from tkinter import *
# Forming GUI
root = Tk()
# Giving title name for GUI
root.title('Calculator')
root.resizable(height=False, width=False)
root.iconbitmap('D:/Python with Corey/Calculator_with_Tkinter/Calculator_ico.ico')
# C:\Users\Acer\Downloads\Calculator_ico.ico

# Making and positioning Entry widget
e = Entry(root, borderwidth=4, width=69, relief='sunken')
e.grid(row=0, column=0, columnspan=4, pady=10, ipady=5)


# function for displaying number that is clicked
def btn_click(number):
    previous_num = e.get()
    e.delete(0, END)
    e.insert(0, str(previous_num) + str(number))

def btn_add():
    global operator
    operator = 'addition'
    global first_num
    first_num = int(e.get())
    e.delete(0, END)

def btn_sub():
    global operator
    operator = 'subtraction'
    global first_num
    first_num = int(e.get())
    e.delete(0, END)

def btn_mul():
    global operator
    operator = 'multiplication'
    global first_num
    first_num = int(e.get())
    e.delete(0, END)

def btn_div():
    global operator
    operator = 'division'
    global first_num
    first_num = int(e.get())
    e.delete(0, END)

def btn_equal():
    second_num = int(e.get())
    e.delete(0,END)
    if operator == 'addition':
        e.insert(0, first_num + second_num)
    elif operator == 'subtraction':
        e.insert(0, first_num - second_num)
    elif operator == 'multiplication':
        e.insert(0, first_num * second_num)
    elif operator == 'division':
        e.insert(0, first_num / second_num)

# function for clearing the screen
def btn_clear():
    e.delete(0,END)

# function for clearing recently entered number  
def btn_back():
    current_num = len(e.get())
    e.delete(current_num-1)


# creating the Button widget
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda:btn_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda:btn_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda:btn_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda:btn_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda:btn_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda:btn_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda:btn_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda:btn_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda:btn_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda:btn_click(0))
# creating button equal and clear
button_equal = Button(root, text='=', padx=92, pady=20, command=btn_equal, bg='#90EE90')
button_clear = Button(root, text='Clear', padx=93.25, pady=20, command=btn_clear, bg='#FF7F7F')
button_back = Button(root, text='Back', padx=93.25, pady=20, command=btn_back, bg='#918F90')
# creating operator buttons
button_add = Button(root, text='+ (add)', padx=40, pady=20, command=btn_add, bg='#FAEBD7')
button_sub = Button(root, text='- (sub)', padx=40, pady=20, command=btn_sub, bg='#FAEBD7')
button_mul = Button(root, text='* (mul)', padx=40, pady=20, command=btn_mul, bg='#FAEBD7')
button_div = Button(root, text='/ (div)', padx=40, pady=20, command=btn_div, bg='#FAEBD7')

# positioning the Button widget
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
# positioning operators buttons
button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_mul.grid(row=3, column=3)
button_div.grid(row=4, column=3)
#positioning equal,back,clear button
button_equal.grid(row=4,column=1, columnspan=2)
button_back.grid(row=5,column=0, columnspan=2)
button_clear.grid(row=5,column=2, columnspan=2)


# looping the screen everytime
root.mainloop()