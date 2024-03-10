def main():
    contacts = {}  # Dictionary to store names and email addresses

    # Function to look up a person's email address
    def lookup_email(name):
        if name in contacts:
            print(f"The email address of {name} is: {contacts[name]}")
        else:
            print(f"No email address found for {name}")

    # Function to add a new name and email address
    def add_contact(name, email):
        contacts[name] = email
        print(f"Added {name}'s email address: {email}")

    # Function to change an existing email address
    def change_email(name, new_email):
        if name in contacts:
            contacts[name] = new_email
            print(f"Changed {name}'s email address to: {new_email}")
        else:
            print(f"No email address found for {name}")

    # Function to delete an existing name and email address
    def delete_contact(name):
        if name in contacts:
            del contacts[name]
            print(f"Deleted {name}'s contact information")
        else:
            print(f"No email address found for {name}")

    # Menu to demonstrate the options
    while True:
        print("\nOptions:")
        print("1. Look up email address")
        print("2. Add new contact")
        print("3. Change email address")
        print("4. Delete contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the name to look up: ")
            lookup_email(name)
        elif choice == '2':
            name = input("Enter the name: ")
            email = input("Enter the email address: ")
            add_contact(name, email)
        elif choice == '3':
            name = input("Enter the name to change email address: ")
            new_email = input("Enter the new email address: ")
            change_email(name, new_email)
        elif choice == '4':
            name = input("Enter the name to delete: ")
            delete_contact(name)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
