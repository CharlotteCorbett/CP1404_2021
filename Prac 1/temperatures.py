"""
CP1404- Practical 1
Charlotte Corbett
Pseudocode for temperature conversion
Get fahrenheit to celsius value from user
Convert fahrenheit to celsius
Display result
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * (9.0 / 5) + 32
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("Farenheit: "))
        celsius = (fahrenheit - 32) * 5.0 / 9
        print("Result:{:.2f} C".format(celsius))
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")