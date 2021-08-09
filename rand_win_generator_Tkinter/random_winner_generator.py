# importing packages
import csv
from random import randint
from tkinter import *
from tkinter.font import BOLD

# creating main GUI called root and assigning title
root = Tk()
root.title('Random Winner Generator')

# extracting data from csv file and appending in "entries" list
entries = []
with open('customer_names.txt','r') as namelist:
    csv_reader = csv.reader(namelist, delimiter=',')
    for person in csv_reader:
        for i in range(len(person)):
            entries.append(person[i])

# function for declaring winner
def winner():
    #converting "entries" into set, so that every value be unique
    set_entries = set(entries)
    # again converting back those set into list
    list_entries = list(set_entries)
    len_entries = len(list_entries)-1
    # generating random number
    rando = randint(0,len_entries)
    win_label = Label(root, text=list_entries[rando], font=(BOLD,20))
    win_label.pack(pady=30)

# creating label for heading
head_label = Label(root, text="Today's Winner:", font=(BOLD,24))
head_label.pack(padx=40 ,pady=20)

# creating button to declare winner
button = Button(root, text="Generate random winner", padx=10, pady=20, command=winner, bg='light yellow')
button.pack(pady=30)

# looping the screen over and over again
root.mainloop()


