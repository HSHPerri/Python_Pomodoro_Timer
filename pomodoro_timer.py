# This file is going to house the final GUI app.
# Need to use tkinter to make a gui for the pomodoro timer.

from tkinter import *
from tkinter.ttk import *


# TODO: Change entry fields to remove blue underline.
# TODO: Change background of timer label to have rounded corners.
# TODO: Find a better way to display app title (Logo?).
# TODO: Find a way to make the button red.


def pomodoro_begin():
    # TODO: Make a start on this by adding pomodoro logic.
    pass


def pomodoro_reset():
    # TODO: Make a function to reset application after use.
    pass


# Initial window setup, title, screensize etc.
root = Tk()
root.title("Pomodoro")
root.geometry("400x350")
root.resizable(False, False)

# Create a title label for the application.
title = Label(text='Pomodoro', font=('helvetica', 40, 'bold'))
title.place(relx=0.5, rely=0.1, anchor=CENTER)

# Create a label for the actual timer function.
timer_display = Label(text='00:00', font=('Arial', 48, 'bold'))
timer_display.place(relx=0.5, rely=0.3, anchor=CENTER)
timer_display.configure(background='light gray', width=6, anchor=CENTER)

# Create a global font tuple for input fields.
input_font = ("Arial", 20, "bold")

# Creating interval input field.
interval_input = Entry()
interval_input.place(relx=0.2, rely=0.65, anchor=CENTER)
interval_input.configure(width=5, font=input_font, justify='center')

# Creating time input field.
time_input = Entry()
time_input.place(relx=0.5, rely=0.65, anchor=CENTER)
time_input.configure(width=5, font=input_font, justify='center')

# Creating break time input field.
break_time_input = Entry()
break_time_input.place(relx=0.8, rely=0.65, anchor=CENTER)
break_time_input.configure(width=5, font=input_font, justify='center')

button_style = Style()
button_style.configure('W.TButton', font='calibri')

# Begin button placement.
start_button = Button(root, text="Begin", padding=12, style='W.TButton')
start_button.place(relx=0.5, rely=0.85, anchor=CENTER)

progress_bar = Progressbar(length=350)
progress_bar.place(relx=0.5, rely=0.5, anchor=CENTER)

# Activate the program's main loop.
root.mainloop()
