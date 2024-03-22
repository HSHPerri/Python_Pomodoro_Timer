# Pomodoro Timer App.
# V1.0.0
# By Harry Perriton

# Import pomodoro logic file/methods.
import pomodoro
from time import sleep

program_on = True
pomodoro.reset_screen()

# Loops program for multiple uses.
while program_on:

    # Check input number of intervals is valid.
    first_input_check = True
    while first_input_check:
        interval_choice = input("How many intervals would you like to study for? ")

        if pomodoro.interval_count_check(interval_choice):
            first_input_check = False
        else:
            continue

    # Check interval time amount is valid.
    second_input_check = True
    while second_input_check:
        interval_time_choice = input("How much time should each interval last? (In whole minutes) ")

        if pomodoro.time_input_check(interval_time_choice):
            second_input_check = False
        else:
            continue

    # Check break time amount is valid.
    third_input_check = True
    while third_input_check:
        break_time_choice = input("How much time would you like for breaks inbetween? (In whole minutes) ")

        if pomodoro.time_input_check(break_time_choice):
            third_input_check = False
        else:
            continue

    # Call the pomodoro timer using the three input values as parameters.
    pomodoro.pomodoro_logic(interval_time_choice, interval_choice, break_time_choice)

    # Reset the screen before moving on.
    pomodoro.reset_screen()

    # Check whether the user wants to restart the program.
    # Match their response to acceptable cases, throw error for unacceptable cases.
    restart_check = True
    while restart_check:
        user_restart_input = input("Would you like to start a new session? (Y/N) ")
        match user_restart_input.lower():
            case "y":
                program_on = True
                restart_check = False
            case "yes":
                program_on = True
                restart_check = False
            case "n":
                program_on = False
                restart_check = False
            case "no":
                program_on = False
                restart_check = False
            case _:
                print("Error: Please enter Y, Yes, N or No as a response.")
                sleep(3)
                pomodoro.reset_screen()
