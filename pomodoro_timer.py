# Pomodoro Timer App.
# V1.1.0
# By Harry Perriton

from tkinter import *
import customtkinter

# TODO: Implement the actual timer functionality within the application.


def pomodoro_begin():
    # TODO: Make a start on this by adding pomodoro logic.
    pass


def pomodoro_reset():
    # TODO: Make a function to reset application after use.
    pass


# ---------------------WINDOW SETUP---------------------------
# Create a global font tuple for input fields.
input_font = ("Arial", 20, "bold")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Initial window setup, title, screensize etc.
root = customtkinter.CTk()
root.title("Pomodoro")
root.geometry("400x350")
root.resizable(False, False)


# ---------------------TITLE LABEL---------------------------
# Title display
title = customtkinter.CTkLabel(root, text="Pomodoro V1.1.0", )
title.place(relx=0.15,
            rely=0.06,
            anchor=CENTER,
            )


# ---------------------TIMER DISPLAY---------------------------
# Create a label for the actual timer function.
timer_display = customtkinter.CTkLabel(root,
                                       text='00:00',
                                       font=('Arial', 80, 'bold')
                                       )

# Place the timer appropriately.
timer_display.place(relx=0.5,
                    rely=0.28,
                    anchor=CENTER
                    )


# ---------------------PROGRESS BAR---------------------------
# Create a progress bar to understand how long the interval has left.
progress_bar = customtkinter.CTkProgressBar(root)

# Place the bar within the application.
progress_bar.place(relx=0.5, rely=0.5, anchor=CENTER)

# Configure the bar's appearance.
progress_bar.configure(width=325,
                       height=15,
                       corner_radius=20,
                       mode="determinate",
                       determinate_speed=5)

# Set a default value of 0 so that it starts from the beginning.
progress_bar.set(0)


# ---------------------INTERVAL INPUT FIELD---------------------------
# Creating interval input field.
interval_input_label = customtkinter.CTkLabel(root,
                                              text="No. Intervals",
                                              )
interval_input_label.place(relx=0.2,
                           rely=0.56,
                           anchor=CENTER,
                           )

interval_input = customtkinter.CTkEntry(root)
interval_input.place(relx=0.2,
                     rely=0.65,
                     anchor=CENTER,
                     )

# Configuring its appearance.
interval_input.configure(width=90,
                         height=40,
                         font=input_font,
                         justify='center',
                         )

# ---------------------TIME INPUT FIELD---------------------------
# Creating time input field.
time_input_label = customtkinter.CTkLabel(root, text="Interval Time", )
time_input_label.place(relx=0.5,
                       rely=0.56,
                       anchor=CENTER,
                       )

time_input = customtkinter.CTkEntry(root)
time_input.place(relx=0.5,
                 rely=0.65,
                 anchor=CENTER,
                 )

# Configuring its appearance.
time_input.configure(width=90,
                     height=40,
                     font=input_font,
                     justify='center',
                     )

# ---------------------BREAK TIME INPUT FIELD---------------------------
# Creating break time input field.
break_time_input_label = customtkinter.CTkLabel(root, text="Break Time", )
break_time_input_label.place(relx=0.8,
                             rely=0.56,
                             anchor=CENTER,
                             )

break_time_input = customtkinter.CTkEntry(root)
break_time_input.place(relx=0.8,
                       rely=0.65,
                       anchor=CENTER,
                       )

# Configuring its appearance.
break_time_input.configure(width=90,
                           height=40,
                           font=input_font,
                           justify='center',
                           )

# ---------------------START BUTTON---------------------------
# Begin button placement.
start_button = customtkinter.CTkButton(root,
                                       text="Begin",
                                       height=50,
                                       width=200,
                                       font=("calibri", 24, "bold"),
                                       )

start_button.place(relx=0.5, rely=0.85, anchor=CENTER)

# Activate the program's main loop.
root.mainloop()
