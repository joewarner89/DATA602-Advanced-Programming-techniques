#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

HIGH_SCORE = 95
 
# Get the test scores.
#adding int or float
test1 = float(input('Enter the score for test 1: '))
test2 = float(input('Enter the score for test 2: '))
# new variable added
test3 = float(input('Enter the score for test 3: '))
# Calculate the average test score.
## Adding ()
average = (test1 + test2 + test3) / 3

# Print the average.
print('The average score is', average)
# If the average is a high score,
# congratulate the user.
# Change it to capitol letters high score
if average >= HIGH_SCORE:
    print('Congratulations!')
print('That is a great average!')

#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 
print("We are going to calculate the area of a rectangle")
width = float(input("Enter the width: "))
length = float(input("Enter the length: "))
area = length * width
print(f"The area of a rectangle is {area}")
#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.

# name of person
name = input("Enter your name, Please! ")
age = int(input("Enter your age: "))

print(f"Happy birthday, {name}! You are {age} years old today!")

#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"


