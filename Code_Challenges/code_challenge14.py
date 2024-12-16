def code_challenge14():

    print("Good day, user!")
    human = input("Please enter your name: ")

    count = 0
    isContinue = True

    while isContinue:
        user_input = input(f"Hi {human}, please enter a number (or type 'stop' to end): ")

        if user_input.lower() == "stop":
            print("Loop has been terminated")
            print(f"{human}, the sum of the numbers you have entered is {count}")
            isContinue = False 
            
        elif user_input.isdigit():  
            num = int(user_input)  
            count += num
        else:
            print("Invalid answer. Please enter a valid number or 'stop' to terminate.")
