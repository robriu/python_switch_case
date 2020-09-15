### Allows to define a flexible menu. ###

def default(msg = "Wrong Option"):
	print(msg)
	return -1	# aoid comparing strings in processing further.

# can print something.
def option1():
	return "Choice 1"

# can set variables/flag values.
def option2(a = True):
	return True and a

# can do more complicated operations.
def option3(a = 5, b = 3):
	return a + b

# structure for switch statement.
switch = {
		0: default,
		1: option1,
		2: option2,
		3: option3
	}

# define process func.
def switch_process(case):
	choice = switch.get(case, default)
	return choice
