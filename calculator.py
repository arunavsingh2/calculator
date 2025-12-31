# ===============================
# PROGRAM: Simple Calculator
# AUTHOR: Beginner Python Project
# ===============================

# This loop keeps the calculator running until the user chooses to exit
while True:

    # Display calculator menu
    print("""
    1 - ADDITION
    2 - SUBTRACT
    3 - MULTIPLY
    4 - DIVIDE
    5 - EXIT
    """)

    # Take operation input safely
    try:
        operation = int(input("Select your input: "))
    except ValueError:
        # Runs if user enters non-numeric input
        print("Please enter a number only.")
        continue  # Go back to menu

    # Exit condition
    if operation == 5:
        print("Calculator Closed.")
        break  # Stop the loop and end program

    # Check if the selected operation is valid
    if operation in [1, 2, 3, 4]:

        # Take number inputs safely
        try:
            num_1 = int(input("Enter your 1st number: "))
            num_2 = int(input("Enter your 2nd number: "))
        except ValueError:
            # Runs if user enters alphabets or symbols
            print("Invalid Entry! Please enter numbers only.")
            continue  # Go back to menu

        # Perform addition
        if operation == 1:
            print("Result:", num_1 + num_2)

        # Perform subtraction
        elif operation == 2:
            print("Result:", num_1 - num_2)

        # Perform multiplication
        elif operation == 3:
            print("Result:", num_1 * num_2)

        # Perform division with zero check
        elif operation == 4:
            if num_2 == 0:
                print("Cannot divide by zero.")
            else:
                print("Result:", num_1 / num_2)

    # Runs if operation number is not between 1 and 5
    else:
        print("Invalid selection! Please choose between 1 and 5.")
