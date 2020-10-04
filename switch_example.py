from switch import switch, switch_process, default

### Please note: this is an example, not a solution. ###
### Code was simplified for the ease of understanding. ###

# Example of printing switch data.
# print(switch_process(int(input("Choose an option: ")))())

# Example of further switch data processing.
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
        # Can be replaced to return function for dynamic inputs.
        a, b = 10, 20   # change to play
        res = choice(a, b)
        print(f"Option 3: {a} + {b}: {res}")
        
    # Can be used as: choice()
    print(choice())
    