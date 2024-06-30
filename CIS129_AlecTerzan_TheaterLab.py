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
  total = 0
  subtotal = 0

  print('Hello and welcome to the Theatrical Phenomenon!\n')
  response1 = input('Do you want to change the prices or number of seats in a section before starting?\n')
  if response1 == 'yes':
    response2 = input('Do you want to change the prices of seating?\n')
    if response2 == 'yes':
      response3 = input('What section do you want to change the pricing?\n')
      if response3 == 'A':
        A = int(input('What price do you want it set at?\n')
      elif response3 == 'B':
        B = int(input('What price do you want it set at?\n')
      elif response3 == 'C':
        C = int(input('What price do you want it set at?\n')
    response4 = input('Do you want to change number of seats in a section?\n')
    if response4 == 'yes':
      response5 = input('What section do you want to change seating?\n')
      if response5 == 'A':
        A = input('How many seats will be in this section?\n')
      elif response5 == 'B':
        B = input('How many seats will be in this section?\n')
      elif response5 == 'C':
        C = input('How many seats will be in this section?\n')
  
  Aseats = int(input('How many tickets were sold in section A?\n'))
  while isNumberValid(Aseats, A) == False:
    Aseats = int(input('How many tickets were sold in section A?\n'))
  subtotal += Aseats
  print('Subtotal: $', subtotal)
  
  Bseats = int(input('How many tickets were sold in section B?\n'))
  while isNumberValid(Bseats, B) == False:
    Bseats = int(input('How many tickets were sold in section B?\n'))
  subtotal += Bseats
  print('Subtotal: $', subtotal)
  
  Cseats = int(input('How many tickets were sold in section C?\n'))
  while isNumberValid(Cseats, C) == False:
    Cseats = int(input('How many tickets were sold in section C?\n'))
  subtotal += Cseats
  print('Subtotal: $', subtotal)

def isNumberValid(user_seats, seats):
  if user_seats < seats and user_seats > 0 and user_seats % 1 == 0:
    return True
  else:
    return False
