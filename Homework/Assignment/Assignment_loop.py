# Q1 Write a program that prompts the user for a meal: breakfast, lunch, or dinner.
# Then using if statements and else statements print the user a message recommending a meal.
# For example, if the meal was breakfast, you could say something like, “How about some bacon and eggs?”
# The user may enter something else in, but you only have to respond to breakfast, lunch, or dinner.

done= False

while not done:
    print("Menu")
    print("What meal are you planning: breakfast, lunch, or dinner? ")
    print("D - Dinner ")
    print("L - Lunch " )
    print("B - Breakfast ")
    print("Q - for Exiting" )
    choice = input("Please make choice: ")
    if choice == "B":
        print("How about some bacon and eggs?")
    elif choice == "L":
        print("How about a sandwich or a salad?")
    elif choice == "D":
        print("How about some rice and beans with chicken. ")
    elif choice == "Q":
        print("Thank you for your order! ")
        done = True

# Q2 The mailroom has asked you to design a simple payroll program that calculates a student
# employee’s gross pay, including any overtime wages. If any employee works over 20 hours in a week,
# the mailroom pays them 1.5 times their regular hourly pay rate for all hours over 20.
# You should take in the user’s input for the number of hours worked, and their rate of pay.

# hours worked and pay rate
hours = float(input("Enter the number of hours worked this week: "))
pay_rate = float(input("Enter the hourly pay rate: $"))

# Calculating regular pay and overtime pay
if hours <= 20:
    gross_pay = hours * pay_rate
else:
    # regular pay
    reg_hours_pay = 20 * pay_rate
    # overtime hours
    ov_hours = hours - 20
    # overtime_pay with 1.5 time the pay rate
    ov_pay = ov_hours * (pay_rate * 1.5)
    gross_pay = reg_hours_pay + ov_pay

# Displaying the gross pay
print("Gross pay for the week: $", format(gross_pay, '.2f'))

# Q3 Write a function named times_ten. The function should accept an argument and display the product
# of its argument multiplied times 10.


number = int(input("Please, inter a number: "))

def times_ten(num):
    result = num * 10
    return result


print(f"The product {number} multiplied by 10 is {times_ten(number)}")


# SQ4 Find the errors, debug the program, and then execute to show the output.

def main():
    calories1 = float(input("How many calories are in the first food? "))
    calories2 = float(input("How many calories are in the second food? "))
    showCalories(calories1, calories2)

def showCalories(calories1, calories2):
    total_calories = calories1 + calories2
    print("The total calories you ate today:", format(total_calories, '.2f'))

# Call the main function to start the program
main()

#Q5 Write a program that uses any loop (while or for) that calculates the total of the following series of numbers:
#                               1/30 + 2/29 + 3/28 ............. + 30/1


total = 0

for i in range(1, 31):
    total += i / (31 - i)

print("The total of the series is:", total)

# Q6 Write a function that computes the area of a triangle given its base and height.
# The formula for an area of a triangle is:
# AREA = 1/2 * BASE * HEIGHT
#
# For example, if the base was 5 and the height was 4, the area would be 10.
# triangle_area(5, 4)   # should print 10


def main():
    BASE = float(input("Enter the base of a triangle: "))
    HEIGHT = float(input("Enter the height of a triangle: "))
    triangle_area(BASE, HEIGHT)
    print(f"The area of the triangle base {BASE} and height {HEIGHT} is {triangle_area(BASE,HEIGHT)}")


def triangle_area(BASE, HEIGHT):
    area = (BASE * HEIGHT) / 2
    return area


main()

