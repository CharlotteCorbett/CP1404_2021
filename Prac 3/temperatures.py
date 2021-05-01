"""Temperatures.py with functions"""


def main():
    # get choice
    MENU, choice = get_choice()
    # calculate temperature
    while choice != "Q":
        if choice == "C":
            calculate_celsius()
        elif choice == "F":
            calculate_fahrenheit()
        else:
            print_error()
        MENU, choice = get_choice()
    print("Thank you.")


def print_error():
    print("Invalid option")


def calculate_fahrenheit():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5.0 / 9
    print("Result:{:.2f} C".format(celsius))


def calculate_celsius():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * (9.0 / 5) + 32
    print("Result: {:.2f} F".format(fahrenheit))


def get_choice():
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    return MENU, choice


main()