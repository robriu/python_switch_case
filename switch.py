### Define flexible menu. ###

def default(msg = "Wrong Option"):
    print(msg)
    return -1    # Avoid comparing strings in further processing.

# Print anything you want.
def option1():
    return "Choice 1"

# Set variable/flag values.
def option2(a = True):
    return True and a

# And more complicated operations.
def option3(a = 5, b = 3):
    return a + b

# Structure for switch statement.
switch = {
        0: default,
        1: option1,
        2: option2,
        3: option3
    }

# Define process functions.
def switch_process(case):
    choice = switch.get(case, default)
    return choice
