done = False
contacts = {}

# function that can loook for someone email
def mail_search(name):
    if name in contacts:
        print(f"The email address of {name} is : {contacts[name]}" )
    else:
        print(f"there is no information avalialble for {name}")

def add_contact(name, email):
    contacts[name] = email
    print(f"the name {name} and email {email} has been added to the contact" )

def change_contact(name, email):
    if name in contacts:
        
        contacts[name] = new_email
        print(f"name {name} and email {new_email} has been changed! ")
    else:
        print(f"No email address found for name {name}")
    

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"name {name} has been deleted for contanct")

    else:
        print("No email address has been found fpr name {name}")

while not done:
    print("Menu")
    print("A - Search for email address")
    print("B - Add new contact")
    print("C - Change email from contact")
    print("D - Delete recordsd from contact")
    print("Q - Exit")

    choice = input("Please carefully enter your choice: ")
    if choice == "A":
        name = input("Enter the name to look up: ")
        mail_search(name)

    elif choice == "B":
        name = input("Enter the name: ")
        email = input("Enter the email address: ")
        add_contact(name,email)

    elif choice == "C":
        name = input("Enter the name to change email address: ")
        new_email = input("Enter the new email address: ")
        change_contact(name, email)
    elif choice == "D":
        name = input("Enter the name to delete: ")
        delete_contact(name)
    elif choice == "Q":
        print("Your are exitting the application ")
        print("Here is your final dictionary: \n")
        for key, value in contacts.items():
            
            print(key,value)
        done = True
        
