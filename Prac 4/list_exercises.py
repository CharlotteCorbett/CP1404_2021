# Basic list operations
# numbers = []
# for number in range(5):
#     numbers.append(int(input("Number:")))
# print("The first number is {}\n"
#       "The last number is {}\n"
#       "The smallest number is {}\n"
#       "The largest number is {}\n"
#       "The average of the numbers is {}\n"
#       .format(numbers[0], numbers[4], min(numbers),
#               max(numbers), sum(numbers)))
# 2. Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
             'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole',
             'InterpreterInterface', 'StartServer', 'bob']
user_input = input("Password?:")
if user_input in usernames:
    print("Access granted")
else:
    print("Access denied")
