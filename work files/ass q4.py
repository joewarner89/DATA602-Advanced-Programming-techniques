done= False
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
    print("Here is your class information: " )
    for key,value in room_numbers.items():
        print(key)

        
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
            print(f"\nInstructor: {instructor} " )
            print(f"\nSchedule Time: {schedule_time}")

        else:
            print("Course number not found")


    elif choice == "Q":
        print("Thanks for Exiting! ")
        done=True
        
