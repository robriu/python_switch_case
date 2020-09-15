### Allows to define a flexible menu ###

def default():
	return print("Wrong Option")

# can print something.
def option1():
	return "option 1"

# can set variables/flag values.
def option2():
	return True

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

# define process func
def switch_process(case):
	choice = switch.get(case, default)
	return choice
		
# Use example when switch data is printed.
# print(switch_process(int(input("Choose an option: ")))())

# Use example when switch data is processed further.
temp = switch_process(int(input("Choose an option: ")))
print(temp())

# Find out the type for further processing.
# print(type(temp()))
