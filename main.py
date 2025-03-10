#############
#Section 1 - Import Modules and Global Variables
import random

# Define a shared product list for consistency across functions
product_list = [Product(random.randint(100000, 999999)) for _ in range(10)]
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
    print(f"Welcome {name}! Oh to be {age} again! How can I help you today?")

def display_menu():
    print("\n **Please choose from the following options:**")
    print("1. Return item")
    print("2. Exchange item")
    print("3. Exit the conversation")

def user_selection():
    # Program starts with in_use = True, indicating the program is running
    in_use = True
    while in_use:
        try:
            user_input = int(input("Enter a number between 1-3: "))
            if user_input == 1:
                return_item()
            elif user_input == 2:
                exchange_item()
            elif user_input == 3:
                print("Goodbye! Thank you for your time!")
                # Exiting the program
                in_use = False
            else:
                print("\nSorry, not a valid choice. Please try again.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def return_item():
    # Print product list
    print("Available product IDs:", [product.prod_Id for product in product_list])
    product_id = input("Please enter a product ID (6-digit code on your receipt): ")

    # Input validation
    if not product_id.isdigit() or len(product_id) != 6:
        print("Invalid Product ID. Please enter a 6-digit numeric code.")
        return

    # Check if product ID exists
    if any(str(product.prod_Id) == product_id for product in product_list):
        print(f"Product {product_id} found. Processing return.")
    else:
        print(f"Product {product_id} not found. Please check the ID and try again.")

def exchange_item():
    # Print product list
    print("Available product IDs:", [product.prod_Id for product in product_list])

    user_product_id = input("Please enter a product ID (6-digit code on your receipt): ")
    chosen_product_id = input("Please enter the product ID of the item you'd like in exchange: ")

    # Input validation
    if not user_product_id.isdigit() or len(user_product_id) != 6:
        print("Invalid Product ID. Please enter a 6-digit numeric code for the product to return.")
        return
    if not chosen_product_id.isdigit() or len(chosen_product_id) != 6:
        print("Invalid Product ID. Please enter a 6-digit numeric code for the product to exchange.")
        return

    # Check if both product IDs exist
    if any(str(product.prod_Id) == user_product_id for product in product_list) and \
       any(str(product.prod_Id) == chosen_product_id for product in product_list):
        print(f"Product {user_product_id} found. Processing exchange for product {chosen_product_id}.")
    else:
        print(f"Product {user_product_id} or {chosen_product_id} not found. Please check the IDs and try again.")
#############


#############
#Section 3 - Class Definition
class Product:
    def __init__(self, prod_id):
        # Generate a random product ID between 1000 and 5000
        self.prod_Id = prod_id
#############


#############
#Section 4 - Running Section
greeting()
display_menu()
user_selection()
#############
