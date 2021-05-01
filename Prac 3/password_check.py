"""Password checker"""


def main():
    # Write initial code for password checker
    is_correct_length = get_password()
    print_password(is_correct_length)


def print_password(is_correct_length):
    for letter in range(is_correct_length):
        print('*', end='')


def get_password():
    user_password = input("Password?:")
    is_correct_length = len(user_password)
    if is_correct_length < 10:
        while is_correct_length < 10:
            print("Invalid password")
            user_password = input("Password?:")
            is_correct_length = len(user_password)
    return is_correct_length


main()