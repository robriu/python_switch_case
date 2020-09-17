from switch import switch, switch_process, default

### Example code on how to get and operate with choice types. ###
### Please note that is an example of use, not a solution. ###
### Code was simplified for ease of understanding. ###

# Use example when switch data is printed.
# print(switch_process(int(input("Choose an option: ")))())

# Use example when switch data is processed further.
choice = switch_process(int(input("Choose an option: ")))

# if choice wasn't default.
if choice != switch[0]:
    if choice == switch[1]:
        print(f"Option 1: {choice()}")

    if choice == switch[2]:
        input_flag = False   # change to play
        res = choice(input_flag)
        print(f"Option 2: True and {input_flag}: {res}")

    if choice == switch[3]:
        # Can be replaced with get function to have dynamic input.
        a, b = 10, 20   # change to play
        res = choice(a, b)
        print(f"Option 3: {a} + {b}: {res}")
        
    # Can be used as: choice()
    print(choice())
    