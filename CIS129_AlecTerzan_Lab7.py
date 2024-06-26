# Alec Terzan
# Lab 7 Dice Game
# Create a dice game using random number generator and user input
# 6/25/2024

# Import libraries
import random

def main():
  print()
  
  # Initialize variables
  EndProgram ='no'
  playerOne = 'NONAME'
  playerTwo = 'NONAME'
  # Set players' name to input
  playerOne, playerTwo = inputNames(playerOne, playerTwo)
  # Set up a while loop
  while endProgram == 'no':
    # declare varaibles
    winnerName = 'NO NAME'
    p1number = 0
    p2number = 0
    # call rollDice to winnerName
    winnerName = rollDice(p1number, p2number, playerOne, playerTwo, winnerName)
    # display information after rollDice executes
    displayInfo(winnerName)
    # asks user to continue
    endProgram = input('Do you want to end program? (yes/no):')
# create inputName function to get player names
def inputNames(playerOne, playerTwo):
  playerOne = input("What is Player One's name?: ")
  playerTwo = input("What is Player Two's name?: ")
  return playerOne, playerTwo
# create rollDice function to roll dice for each player
def rollDice(p1number, p2number, playerOne, playerTwo, winnerName):
  p1number = random.randomint(1, 6)
  p2number = random.randomint(1, 6)
  if p1number > p2number:
    winnerName = playerOne
  elif p2number > p1number:
    winnerName = playerTwo
  elif p1number == p2number:
    winnerName = 'TIE'
  return winnerName
# create function to display winner
def displayInfo(winnerName):
  print(winnerName)
