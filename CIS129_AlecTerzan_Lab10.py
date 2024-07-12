# Alec Terzan
# Lab 10
# Print an entered amount into check - protected format
# 7/10/2024
# set up input string variable
number = input()

# set up check format with astericks
cformat = ''
for i in range(10 - len(number)):
    cformat += '*'
# print the input number with the format
print(cformat + number)
# print barrier
iformat = '-'
iformat *= 10
print(iformat)
# set up other format with 0s instead of astericks
pformat = ''
for i in range(10 - len(number)):
    pformat += '0'
pnumber = ''
pnumber += number.replace('.', '0')
# print format with astericks along with printed number with zeroes in place of non-number characters
print(pformat + pnumber.replace(',','0'))