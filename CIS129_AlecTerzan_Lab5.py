# Alec Terzan
# 6/21/2024
# Lab 5 Bottle Return Program
# Create a program that calculates the total bottles returned and payout for the week using loops.

# Declare variables
totalBottles = 0
todayBottles = 0
totalPayout = 0
counter = 1
NBR_OF_DAYS = 7
keepGoing = 'y'

while keepGoing == 'y':
  # while loop for user to input bottles for each day and calculate total bottles  for the week
  totalBottles = 0
  counter = 1
  while counter <= NBR_OF_DAYS:
    print("Enter number of bottles for day #", counter, ":")
    todayBottles = int(input())
    totalBottles += todayBottles
    counter += 1
  print('\n')
  # a function to calculate total payout for the week
  totalPayout = 0
  totalPayout = totalBottles * 0.10

  # While loop that prints number of bottles and total payout for the week, then asks
  # user to continue with another week of data

  print('The total number of bottles collected is', totalBottles)
  print(f'The total paid out is $ {totalPayout:.2f}')
  print('\n')
  keepGoing = input("Do you want to enter another week's worth of data? \n (Enter y or n) : ")
  print('\n')
