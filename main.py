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
  print("2. Exchange item")
  print("3. Exit the conversation")


def user_selection():
    #when prpgram starts it will be assigned to true, indicating the program is in use/running
    in_use = True
    while in_use:
        display_menu()
        user_input=int(input("Enter a number between 1-4:"))
        if user_input == 1:
            return_item()
        elif user_input == 2:
            exchange_item()
        elif user_input == 3:
            print("Goodbye! Thank you for your time!")
        #this allows the user to exit the game as we're indicating that the program is not in use
            in_use = False
        else:
            print("\nSorry, not a valid choice. Please try again. ")

def return_item():
    #creates a list of 10 random product ids
    product_list = [Product(random.randint(100000, 999999)) for _ in range(10)]
    #prints every product id
    print("Available product IDs:", [product.prod_id for product in product_list])

    product_id = input(str("Please enter a product ID (6-digit code on your receipt): "))

    #iterates thorugh the list to check if the user input ID matched any product in the list
    #ensures that both the input and the other are strings to compare
    if any(str(product.prod_id) == product_id for product in product_list):
        print(f"Product {product_id} found. Processing return.")
    else:
        print(f"Product {product_id} not found. Please check the ID and try again.")

def exchange_item():
    user_input2 = int(input("Please enter a product ID"));




#############
#Section 3 - Class Definition
class Product:
    def __init__(self, prod_id):
            #Generate a random product ID between 1000 and 5000, since its random we dont put it in the parameters
            self.prod_Id = prod_id
#############



#############
#Section 4 - Running Section
greeting()
display_menu()
user_selection()
#############
