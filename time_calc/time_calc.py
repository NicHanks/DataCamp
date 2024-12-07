
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



import tkinter 
from tkinter.constants import * 
tk = tkinter.Tk() 
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2) 
frame.pack(fill=BOTH,expand=1) 
label = tkinter.Label(frame, text="Hello, World") 
label.pack(fill=X, expand=1) 
button = tkinter.Button(frame,text="Exit",command=tk.destroy) 
button.pack(side=BOTTOM) 
tk.mainloop()


# MEAT cutting time calculator

def create_type_of_slice(time_it_takes_to_slices):
    """Return a function that can calculate how long it's going to take"""

    # Define inner_echo
    def number_of_slices(number_of_slices):
        """Calculates time it takes to cut"""
        total_time = time_it_takes_to_slices * number_of_slices
        return total_time

    # Return inner_echo
    return number_of_slices

# easy cut
cut1 = create_type_of_slice(3)

# tougher cut to do so it takes more time
cut2 = create_type_of_slice(9)

# Calculates time to do 3 cuts with a "cut1" type
print(cut1(3), cut2(8),cut1(50000000),"seconds")

name_of_cut = input(print("Okay, now, tell me the name of the cut: "))
time_to_make_that_cut = int(input(print("That's great! Now tell me how long it takes to make that cut: (in seconds) ")))
number_of_cuts = int(input(print("Now one last thing, how many cuts do you plan to make? ")))
users_cut = create_type_of_slice(time_to_make_that_cut)


user = create_type_of_slice(name_of_cut)
print(f"Congratulations on using nic's software! to complete {number_of_cuts} {name_of_cut} cuts it would take {str(users_cut(number_of_cuts))} seconds. ")

#Next, create a list for the users to pick and choose from | and make sure when they're about to pic, they know how long it takes to make the cut. 
