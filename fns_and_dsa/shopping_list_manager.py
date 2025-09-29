#Shopping List Manager
def display_menu():
    """offers menu options to the user."""
    print("Shopping List Manager") 
    print("1. Add Item") 
    print("2. Remove Item") 
    print("3. View List") 
    print("4. Exit") 

def main(): 
    """This function manages the shopping list."""
    shopping_list = []
    while True: 
        display_menu() 
        choice = input("Enter your choice: ")

        if choice == "1": 
            #prompt the user to add an item 
            choice = input("Enter the item to add: ") 
            shopping_list.append(choice) 

        elif choice == "2" : 
            #prompt the user to remove an item 
            choice = input("Enter the item to remove: ") 
            if choice not in shopping_list : 
                print(f"{choice} not found")
            else :
                shopping_list.remove(choice) 

        elif choice == "3" : 
            #display the shopping list to the console
            print(shopping_list)                

        elif choice == "4" : 
            #exit the program 
            print("Goodbye!")
            break 

        else : 
            print("Invalid choice. Please try again.")

if __name__ == "__main__" : 
    main() 






