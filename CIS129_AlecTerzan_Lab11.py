# Alec Terzan
# Lab 11
# Complete Exercises 9.1, 9.2, and 9.3
# 7/18/2024

# Exercise 9.1
# Use with to open the crasete and open a text file
with open("grades.txt", mode = 'w') as grades:
    # Set up a loop that enters as many students' grades as specified by user
    i = int(input('How many grades will be entered?:\n'))
    for x in range(i):
        grades.write(input("Please enter the first name, last name, and grade of a student\n") + '\n')

# Exercise 9.2
with open("grades.txt", mode = 'r') as grades:
    # Print display layout
    print(f'{"First Name":<12}{"Last Name":<12}{"Grade":<12}{"Count":<12}{"Total":<12}{"Average":<8}')
    # Format to display grades properly
    count = 0
    total = 0
    average = 0
    # Print data in correct format
    for record in grades:
        FirstName, LastName, grade = record.split()
        count += 1
        total += int(grade)
        average = total / count
        print(f'{FirstName:<12}{LastName:<12}{grade:<12}{count:<12}{total:<12}{average:>.2f}')

# Exercise 9.3
import csv
with open ('grades.csv', mode = 'w', newline = '\n') as grades:
    i = int(input('How many grades will be entered?:\n'))
    writer = csv.writer(grades)
    for x in range(i):
        writer.writerow([input("Please enter the first name of the student\n"), input("Please enter the last name\n"), input("Please enter the grade for exam 1\n"),  input("Please enter the grade for exam 2\n"), input("Please enter the grade for exam 3\n")])

with open ('grades.csv', mode = 'r', newline = '\n') as grades:
    reader = csv.reader(grades)
    for record in grades:
        print(f'{record}')
