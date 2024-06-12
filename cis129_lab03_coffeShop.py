# Alec Terzan
# 6/12/2024
# Print a reciept for a coffee shop using user input data and calculations to determine total cost

print('********************************************************\n')
print('Coffe Shop Emporium \n')
# Set a value to the user input of coffees for total value
value1 = input('Number of coffees bought?\n')
# Set a different value to the user input of muffins for total value
value2 = input('Number of muffins bought?\n')
print('********************************************************\n\n')
print('********************************************************\n')
# Print how many of each item is bought
if value1 == 1:
  print(value1, 'Coffee bought\n')
else:
  print (value1, 'Coffees bought\n')
if value2 == 1:
  print(value2, 'Muffin bought\n')
else:
  print(value2, 'Muffins bought\n')

value1 = float(value1)
value2 = float(value2)
tax = sum(value1, value2) * 0.06
total = tax + value1 + value2
print('-----')
print('Total: ', total, '\n')
print('********************************************************\n')
