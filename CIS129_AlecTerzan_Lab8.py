# Alec Terzan
# Lab 8
# Create a program to test if a word is a palindrome
# 6/29/2024

# Ask user for a word
word = input('What word do you want to test?\n')

# Put word into array called stack
stack = []
i = 0
for i in range(len(word)):
    stack.append(word[i]) 

# Check if word is palindrome
def is_palindrome(test):
    punctuation_list = [' ', ',', '.', '/', '<', '>', '?', ':', ';', '"', "'", '[', ']', '!', '$', '&', '%', '#', '@', ')', '(', '*', '^', '_', '-', '+', '=', '`', '~', '|']
    y = 1
    x = 0
    while x in range(y):  
        if test[x] in punctuation_list:
            del test[x]
        x += 1
        y = len(test)
    forward = test[:]
    backward = test[::-1]
    item = 0
    for item in range(len(test)):
        forward[item] = forward[item].lower()
        backward[item] = backward[item].lower()
    if forward == backward:
        print('True')
    elif forward != backward:
        print('False')
    test = []
    forward = []
    backward = []

is_palindrome(stack)
