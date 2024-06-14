# Module 4 Lab-4
# Alec Terzan
# 6/13/2024
# The program determines a store and employee bonus based on user input sales increase values.
# Declare necessary variables
storeAmount = 0
empAmount = 0
salesIncrease = 0
monthlySales = 0
prompt = 'Enter amount:\n'
# This gets the monthly sales
monthlySales = float(input(prompt))
# This determines the store bonus based on monthly sales
if monthlySales >= 110000:
  storeAmount = 6000
elif monthlySales >= 100000:
  storeAmount = 5000
elif monthlySales >= 90000:
  storeAmount = 4000
elif monthlySales >= 80000:
  storeAmount = 3000
else:
  storeAmount = 0
# This code determines employee bonuses based on sales increase percentage
# This defines the sales increase percentage and divides by hundred for decimal form
salesIncrease = float(input(prompt))
salesIncrease = salesIncrease / 10
# This determines employee bonus based on sales increase amount
if salesIncrease >= 0.05:
  empAmount = 75
elif salesIncrease >= 0.04:
  empAmount = 50
elif salesIncrease >= 0.03:
  empAmount = 40
else:
  empAmount = 0
# This prints bonus information
print('The store bonus amount is $', storeAmount)
print('The employee bonus amount is $', empAmount)
# Prints special message if all possible bonuses are met
if (storeAmount == 6000) and (empAmount == 75):
  print('Congrats! You have reached the highest bonus amounts possible! ')
