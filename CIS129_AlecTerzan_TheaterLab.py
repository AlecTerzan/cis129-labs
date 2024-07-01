# Alec Terzan
# Theater Seating Lab
# Program for user to purchase seats in a theater for three sections and three price points
# 6/30/2024

def main():
  A = 300
  B = 500
  C = 200
  Acost = 20
  Bcost = 15
  Ccost = 10
  Atotal = 0
  Btotal = 0
  Ctotal = 0
  subtotal = 0
  A, B, C, Acost, Bcost, Ccost = displayMenu(A, B, C, Acost, Bcost, Ccost)
  displayInfo(A, B, C, Acost, Bcost, Ccost)
  A = float(A)
  B = float(B)
  C = float(C)
  Acost = float(Acost)
  Bcost = float(Bcost)
  Ccost = float(Ccost)
  Aseats = float(input('How many tickets were sold in section A?\n'))
  while isNumberValid(Aseats, A) == False:
    Aseats = float(input('How many tickets were sold in section A?\n'))
  Atotal = Aseats * Acost
  subtotal += Atotal
  print(f'Subtotal: ${subtotal:.2f}')
  
  Bseats = float(input('How many tickets were sold in section B?\n'))
  while isNumberValid(Bseats, B) == False:
    Bseats = float(input('How many tickets were sold in section B?\n'))
  Btotal = Bseats * Bcost
  subtotal += Btotal
  print(f'Subtotal: ${subtotal:.2f}')
  
  Cseats = float(input('How many tickets were sold in section C?\n'))
  while isNumberValid(Cseats, C) == False:
    Cseats = float(input('How many tickets were sold in section C?\n'))
  Ctotal = Cseats * Ccost
  subtotal += Ctotal
  print(f'Total: ${subtotal:.2f}')

def isNumberValid(user_seats, seats):
  if user_seats <= seats and user_seats >= 0 and user_seats % 1 == 0:
    return True
  else:
    return False

def displayMenu(seat1, seat2, seat3, cost1, cost2, cost3):
  print('Hello and welcome to the Theatrical Phenomenon!\n')
  print('Number of seats in section A:', seat1)
  print('Number of seats in section B:', seat2)
  print('Number of seats in section C:', seat3)
  print('Price of seating for each section:')
  print('A: $', cost1)
  print('B: $', cost2)
  print('C: $', cost3)
  response1 = input('Do you want to change the prices or number of seats in a section before starting? (y or n)\n')
  if response1 == 'y' or response1 == 'Y':
    response2 = input('Do you want to change the prices of seating? (y or n)\n')
    while response2 == 'y' or response2 == 'Y':
      response3 = input('What section do you want to change the pricing?\n')
      if response3 == 'A' or response3 == 'a':
        cost1 = float(input('What price do you want it set at?\n'))
      elif response3 == 'B' or response3 == 'b':
        cost2 = float(input('What price do you want it set at?\n'))
      elif response3 == 'C' or response3 == 'c':
        cost3 = float(input('What price do you want it set at?\n'))
      response2 = input('Do you want to change the prices of seating in another section? (y or n)\n')
    response4 = input('Do you want to change number of seats in a section? (y or n)\n')
    while response4 == 'y' or response4 == 'Y':
      response5 = input('What section do you want to change seating?\n')
      if response5 == 'A' or response5 == 'a':
        seat1 = input('How many seats will be in this section?\n')
      elif response5 == 'B' or response5 == 'b':
        seat2 = input('How many seats will be in this section?\n')
      elif response5 == 'C' or response5 == 'c':
        seat3 = input('How many seats will be in this section?\n')
      response4 = input('Do you want to change number of seats in another section? (y or n)\n')
    return seat1, seat2, seat3, cost1, cost2, cost3

def displayInfo(seat1, seat2, seat3, cost1, cost2, cost3):
  print('Hello and welcome to the Theatrical Phenomenon!\n')
  print('Number of seats in section A:', seat1)
  print('Number of seats in section B:', seat2)
  print('Number of seats in section C:', seat3)
  print('Price of seating for each section:')
  print('A: $', cost1)
  print('B: $', cost2)
  print('C: $', cost3)

main()
