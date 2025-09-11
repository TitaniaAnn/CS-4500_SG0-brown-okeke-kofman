"""
TODO: Add explanation of program.

"""
def get_valid_txt(prompt):
    while True:
        try:
            # Get the file name from user
            user_input = input(prompt)

            # Check if ends in .txt
            if user_input.tolower().endswith(".txt"):
                return user_input
            else:
                print("ERROR: Please enter a filename ending with .txt")

filename = get_valid_txt("Enter txt filename(.txt): ")
