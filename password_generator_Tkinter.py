# importing packages
from tkinter import *
from random import sample

# creating GUI and setting title and size
root = Tk()
root.title('Password Generator App')
root.geometry("500x350")

# creating global Label widget but not assigning anything
password_label = Label(root)

# function for generating password
def password_generator():

    # accessing that global Label widget so that it is destroyed first if there is any previous one
    global password_label
    password_label.destroy()

    # local variables
    nums = "0123456789"
    small_alphabet = "abcdefgijk"
    capital_alphabet = "ABCDEMNOR"
    signs = "@!#$%"

    random_password = nums+small_alphabet+capital_alphabet+signs
    length = 10

    # finally generating random password using "random.sample()"
    password = "".join(sample(random_password,length))

    # creating Label widget for password and assigning into that global Label widget
    password_label = Label(root, text=password, font=('Calibri',15))
    password_label.pack(pady=15)
    
# Label widget for heading
heading_label = Label(root, text='Password Generator!!', font=('Calibri',25))
heading_label.pack(pady=15)

# Label for body text
body_label = Label(root, text='Please click below button to generate your password.', font=('Times New Roman',16))
body_label.pack(pady=50)

# Button widget to run the "password_generator" function
pass_gen_button = Button(root, text='Generate Password', padx=35, pady=12, borderwidth=5, bg='light pink', command=password_generator)
pass_gen_button.pack()

# looping the screen
root.mainloop()




