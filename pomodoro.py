# Class for the actual timer functionality.
# Can be instantiated for new countdowns.

# Time Class can be used to create timers. Pomodoro class creates countdowns.
import time
from os import system


def reset_screen():
    """
    Just resets the screen when called.
    """
    system('cls')
    print("Pomodoro Timer App 1.0")


def countdown_timer(input_time):
    """
    Creates divmod of input time variable and then creates countdown timer of minutes and seconds.
    :param input_time:
    """
    # input time is entered in minutes so to use divmod, times by 60.
    input_time = int(input_time)
    input_time *= 60

    # While loop acts as countdown timer.
    while input_time:
        minutes, secs = divmod(input_time, 60)
        timer = '{:02d}:{:02d}'.format(minutes, secs)
        print(timer, end="\r")
        time.sleep(1)
        input_time -= 1


def interval_count_check(input_intervals):
    """
    Function is similar to time input check but has slightly different checks. Returns
    true or false based on success of input string.
    :return:
    """
    try:
        input_intervals = int(input_intervals)

        if input_intervals > 100 or input_intervals < 1:
            print("Error: Please enter a number between 1 and 100.")
            return False
        else:
            return True

    except ValueError:
        print("Error: Please enter a whole number.")
        return False


def time_input_check(input_time):
    """
    Function returns true or false based on positive/negative user input.
    """
    # Check it's an integer value that has been entered.
    try:
        input_time = int(input_time)

        # If no value error raised, check that the number is within the correct range.
        if input_time < 1 or input_time > 60:
            print("Error: Please enter a number of minutes between 1 and 120")
            return False
        else:
            # If the value is within the defined range, continue.
            return True
    except ValueError:
        print("Error: Please enter a whole number of minutes.")
        return False


def pomodoro_logic(input_time, input_intervals, input_break_time):
    """
    Function takes in three input parameters for interval time, # of intervals and break
    time and then goes on to activate pomodoro timer at applied settings.
    """
    # Define an interval counter.
    interval_counter = 1

    # Reset the screen and display initial interval counter.
    reset_screen()
    print(f"Interval {interval_counter} / {input_intervals}")

    # For each interval do the following.
    for interval in range(int(input_intervals)):

        # Activate timer at defined interval time. Once finished reset screen.
        countdown_timer(input_time)
        reset_screen()

        # Re-display interval counter, tell user it's break time.
        print(f"Interval {interval_counter} / {input_intervals}")
        print("Break time!")
        time.sleep(2)

        # Activate break timer, when finished, tell the user and then reset and repeat.
        # Add one to counter and reset screen to make sure it updates.
        # For last check make sure that don't over-count.
        countdown_timer(input_break_time)
        if int(interval_counter) != int(input_intervals):
            print("Next interval...")
            time.sleep(2)
            reset_screen()
            interval_counter += 1
            print(f"Interval {interval_counter} / {input_intervals}")
        else:
            reset_screen()
            print("Finished!")
            time.sleep(2)
