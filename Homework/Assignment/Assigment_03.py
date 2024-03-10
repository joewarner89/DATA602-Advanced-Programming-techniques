# Q1 What will the following code display?

numbers = [1, 2, 3, 4, 5]
print(numbers[1:-5])
# Yes we can  bebug this ouput to show the entire list
# This should print the whole list.
print(numbers[:])



# Q2  Design a program that asks the user to enter a store’s sales for each day of the
# week. The amounts should be stored in a list. Use a loop to calculate the total sales for
# the week and display the result.

# creating an empty list
sales = []
# list of the day
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Enter a number for each day
for day in days:
    sales_amount = float(input(f"Enter sales for the day {day} : $"))
    sales.append(sales_amount)
# create the number of the total sales which is the number of
total_sales = sum(sales)
# display the total of the sales
print(f"The total numbers of sales for the week is :  ${total_sales}")

# Q3
travel_list = ["Barcelona", "Paris", "Amsterdam", "Lagos", "London"]

# prit the list
print(f"this is tghe Original list: {travel_list[:]} ")

# Use the sort() function to arrange your list in order and reprint your list.

travel_list.sort()

print(f"this is the sorted list: {travel_list} ")

# Use the sort(reverse=True) and reprint your list.

travel_list.reverse()

print(f"this is the reverse list: {travel_list} ")

# Q4  Write a program that creates a dictionary containing course numbers and the room
# numbers of the rooms where the courses meet. The program should also create a
# dictionary containing course numbers and the names of the instructors that teach each
# course. After that, the program should let the user enter a course number, then it should
# display the course’s room number, instructor, and meeting time.

# Doing it in Menu style
# exit Variables
done = False
# create 3 dictionary room_numuber , intructor_names and schedule time
room_numbers = {
    'DATA607': 'Room 5001',
    'DATA606': 'Room 4501',
    'DATA602': 'Room 6752',
    'DATA601': 'Room 1241'
}

instructor_names = {
    'DATA607': 'SOlya Malya',
    'DATA606': 'James Bryer',
    'DATA602': 'Nicholas Schettini',
    'DATA601': 'Steven Joe'
}

schedule_time = {
    'DATA607': '5:00 PM - 6:00 PM',
    'DATA606': '4:00 PM - 5:00 PM',
    'DATA602': '6:00 PM - 7:00 PM',
    'DATA601': '7:00 PM - 8:00 PM'
}

while not done:
    # Show only the classroom
    print("Here is your class information: ")
    for key, value in room_numbers.items():
        print(key)
    # Menu list for directing the user to do what he wants
    print("Y - to enter another course and room number")
    print("Q - to Quit ")
    choice = input("Enter Y to enter a course and Q to quit: ")
    if choice == "Y" or choice == "y":
        course_number = input("Enter a course number (example: DATA7800) ")
        if course_number in room_numbers and course_number in instructor_names and course_number in schedule_time:
            room_number = room_numbers[course_number]
            instructor = instructor_names[course_number]
            schedule = schedule_time[course_number]

            print(f"\nCourse: {course_number} ")
            print(f"\nRoom Number: {room_number} ")
            print(f"\nInstructor: {instructor} ")
            print(f"\nSchedule Time: {schedule_time}")

        else:
            print("Course number not found")


    elif choice == "Q":
        print("Thanks for Exiting! ")
        # Exit the loop
        done = True

# Q5 Write a program that keeps names and email addresses in a dictionary as
# key-value pairs. The program should then demonstrate the four options:
# ● look up a person’s email address,
# ● add a new name and email address,
# ● change an existing email address, and
# ● delete an existing name and email address.


done = False
contacts = {}


# function that can loook for someone email
def mail_search(name):
    if name in contacts:
        print(f"The email address of {name} is : {contacts[name]}")
    else:
        print(f"there is no information avalialble for {name}")


def add_contact(name, email):
    contacts[name] = email
    print(f"the name {name} and email {email} has been added to the contact")


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
        add_contact(name, email)

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
            print(key, value)
        done = True



