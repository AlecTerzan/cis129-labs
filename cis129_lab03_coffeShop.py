# Alec Terzan
# Lab 03 for CIS 129
# Print a reciept for a coffee shop using user input data and calculations to determine total cost

print('********************************************************\n')
print('Coffe Shop Emporium \n')
# Set a value to the user input of coffees for total value
value1 = input('Number of coffees bought?\n')
# Set a different value to the user input of muffins for total value
value2 = input('Number of muffins bought?\n')
# Set another value to the number of cookies bought
value3 = input('Number of cookies bought?\n')
#Set a fourth value of number of pastries bought
value4 = input('Number of pastries bought?\n')
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\n')
print('VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV\n')
# Print how many of each item is bought and cost of each purchase
print('Coffee Shop Emporium')
newvalue1 = float(value1) * 5
newvalue2 = float(value2) * 4
newvalue3 = float(value3) * 3
newvalue4 = float(value4) * 6
if value1 == 1:
  print(value1, 'Coffee bought at $5: ', newvalue1,'\n')
else:
  print (value1, 'Coffees bought at $5: ', newvalue1,'\n')
if value2 == 1:
  print(value2, 'Muffin bought at $4: ', newvalue2,'\n')
else:
  print(value2, 'Muffins bought at $4: ', newvalue2,'\n')
if value3 == 1:
  print(value3, 'Cookie bought at $3: ', newvalue3,'\n')
else:
  print(value3, 'Cookies bought at $3: ', newvalue3,'\n')
if value4 == 1:
  print(value4, 'Pastry bought at $6: ', newvalue4,'\n')
else:
  print(value4, 'Pastries bought at $6 ', newvalue4, '\n')
# Calculate total including tax
tax = sum(newvalue1, newvalue2, newvalue3, newvalue4) * 0.06
print('6% Tax: $ ', tax)
total = sum(newvalue1, newvalue2, newvalue3, newvalue4, tax)
print('-----------')
print('Total: ', total, '\n')
print('<><><><><><><><><><><><><><><><><><><><><><><><>\n')
print('Thank you for visiting and come back soon!\n')
