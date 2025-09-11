"""
TODO: Add explanation of program.

"""
# library imports
import sys
import re

# global variables
wordList = []
userList = []

# defined objects
class word:
    def __init__(self, text, count):
        self.text = text
        self.count = count
        
# defined functions
def remove_punctuation(text):
    # 
    pattern = r'[^\w\s-]|(?<!\w)-(?!\w)'
    return re.sub(pattern, '', text)

def userBool(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in ('yes', 'y'):
            return True
        elif user_input in ('no', 'n'):
            return False
        else:
            print("Error: ")

# user input functions
def get_valid_txt(prompt):
    while True:
        # Get the file name from user
        user_input = input(prompt).strip().lower()

        # Check if ends in .txt
        if user_input.endswith(".txt"):
            return user_input
        else:
                print("ERROR: Please enter a filename ending with .txt")

def get_valid_word(prompt):
    while True:
        # Get the file name from user
        user_input = input(prompt).strip().lower()

        # Check if ends in .txt
        if re.fullmatch(r"^[a-zA-Z-]+$", user_input) and not user_input.startswith('-') and not user_input.endswith('-') and not ' ' in user_input:
            return user_input
        else:
            print("ERROR: Please enter a valid word")
                
# read file function
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            # Read file contents
            content = file.read()
            content = remove_punctuation(content).lower()
            temp = content.lower().split()
            for t in temp:
                wordList.append(t)
            return True
    except FileNotFoundError:
        # Throw if file does not exist
        print(f"Error: file '{filename}' not found.")
        return False
    except Exception as e:
        # catch any additional errors
        print(f"An error occured: {e}")
        return False
        

# main execution of program
print("Explanation of program")
while True:
    flag = False
    while not flag:
        filename = get_valid_txt("Enter txt filename(.txt): ")
        flag = read_file(filename)
        
    while flag:
        # Ask user for word
        user_input = get_valid_word("Submit a word(a-z and hyphen): ")
        # Add to user list with count
        userList.append(word(user_input, wordList.count(user_input)))
        flag = userBool("Do you want to enter another word(yes/no)? ")
        
    for w in userList:
        print(f"'{w.text}': '{w.count}'")
        
    input("Press Enter to exit the program.")
    sys.exit()
    
# End of program