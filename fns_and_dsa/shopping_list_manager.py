def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            input_item = input("Enter the item to add: ")
            shopping_list.append(input_item)
            print(f"'{input_item}' has been added to your shopping list.")
        elif choice == '2':
            # Prompt for and remove an item
            input_item = input("Enter the Item to remove: ")
            if input_item in shopping_list:
                shopping_list.remove(input_item)
                print(f"'{input_item}' has been removed from your shopping list.")
            else:
                    print(f"'{input_item}' is not in your shopping list.")
        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("Your Shopping List:")
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print("Your shopping list is empty.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()