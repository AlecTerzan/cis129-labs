# Alec Terzan
# Lab 6
# Produce a program that determines minimum hot dogs and buns needed, and leftover hot dogs and buns for a cookout
# 6/22/2024
# Initialize functions

# Set up getTotalHotDogs function
def getTotalHotDogs(attendees, hotDogs):
  attendees = 0
  hotDogs = 0
  attendees = int(input('How many attendees will be at the cookout? '))
  hotDogs = int(input('How many hot dogs will each attendee get? '))
  total = attendees * hotDogs
  print(total)
  return total

# Set up getResults function
def showResults(total):
  DOGS = 10
  BUNS = 8
  dogsLeft = 0
  bunsLeft = 0
  minDogs = 0
  minBuns = 0
  dogsLeft = (DOGS - total % DOGS) % DOGS
  bunsLeft = (BUNS - total % BUNS) % BUNS
  minDogs = (total / DOGS) + (0 ** (0 ** dogsLeft))
  minBuns = (total / BUNS) + (0 ** (0 ** bunsLeft))
  print('Minimum packages of hot dogs needed ', minDogs)
  print('Minimum packages of hot dog buns needed ', minBuns)
  print('Hot dogs remaining', dogsLeft)
  print('Hot dog buns remaining', bunsLeft)

# Execute program functions
totalHotDogs = 0
totalHotDogs = getTotalHotDogs(0, 0)
showResults(totalHotDogs)
