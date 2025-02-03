#############
#Section 1 - Import Modules and Global Variables
import random
#############


#############
#Section 2 - Functions Definition
def greeting():
    def get_user_name():
        return input("Please enter your name: ")
    def get_user_age():
        return input("Please enter your age: ")
    print("Welcome to Elite 101 Customer Support!")
    name = get_user_name()
    print(f"Hello, {name}!")
    age = get_user_age()
    print(f"Welcome {name}! Oh to be {age} again! How can I help you today?");


def display_menu():
  print("\n **Please choose from the following options:**")
  print("1. Return item")
  print("2. exchange item")
  print("3. Verify return/exchange")
  print("4. Exit the conversation")


def user_selection():
    #when prpgram starts it will be assigned to true, indicating the program is in use/running
    in_use = True
    user_input=int(input("Enter a number between 1-4:"))
    if user_input == 1:
        return_item()
    elif user_input == 2:
        exchange_item()
    elif user_input == 3:
        verify()
    elif user_input == 4:
        print("Goodbye! Thank you for your time!")
        #this allows the user to exit the game as we're indicating that the program is not in use
        in_use = False
    else:
        print("\nSorry, not a valid choice. Please try again. ")

def return_item():
    user_input2 = int(input("Please enter a product ID \n Help: 6 number code on your receipt"));
    user_input2 = Product


def exchange_item():
    user_input2 = int(input("Please enter a product ID"));

def verify():
    user_input2 = int(input("Please enter a product ID"));



#############
#Section 3 - Class Definition
class Product:
    def __init__(self):
            #Generate a random product ID between 1000 and 5000, since its random we dont put it in the parameters
            self.prod_Id = random.randint(100000, 999999)
#############



#############
#Section 4 - Running Section
greeting()
display_menu()
user_selection()
return_item()
exchange_item()
verify()
#############
