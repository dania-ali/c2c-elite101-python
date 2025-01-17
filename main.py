#############
#Section 1 - Import Modules and Global Variables
#############


#############
#Section 2 - Functions Definition
def greeting():
    def get_user_name():
        return input("Please enter your name: ")
    def get_user_age():
        return input("Please enter your age: ")
    print("Welcome to the Elite 101 Chatbot!")
    name = get_user_name()
    print(f"Hello, {name}!")
    age = get_user_age()
    print(f"Welcome {name}! Oh to be {age} again! How can I help you today?")D


def display_menu():
  print("\n **Please choose from the following options:**")
  print("1. Placholder Option ")
  print("2. Placholder Option ")
  print("3. Placholder Option ")
  print("4. Exit the conversation ")


def user_selection():
    #when prpgram starts it will be assigned to true, indicating the program is in use/running
    in_use = True
    user_input=int(input("Enter a number between 1-4:"))
    if user_input == 1:
        Placholder_Option()
    elif user_input == 2:
        Placholder_Option()
    elif user_input == 3:
        Placholder_Option()
    elif user_input == 4:
        print("Goodbye! Thank you for using the program!")
        #this allows the user to exit the game as we're indicating that the program is not in use
        in_use = False
    else:
        print("\nSorry, not a valid choice. Please try again. ")


#############
#Section 3 - Class Definition
#############



#############
#Section 4 - Running Section
greeting()
display_menu()
user_selection()
#############
