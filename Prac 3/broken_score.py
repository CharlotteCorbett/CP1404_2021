"""Broken score with functions"""


def main():
    # user_score = get_user_score()
    user_score = get_random_score()
    if user_score < 0 or user_score > 100:
        print("Invalid score")
    elif user_score >= 90:
        print("Excellent")
    elif user_score >= 50:
        print("Passable")
    elif user_score <50:
        print("Bad")
    else:
        print("Invalid score")


def get_user_score():
    user_score = float(input("Enter score:"))
    return user_score


def get_random_score():
    import random
    user_score = random.randint(-5, 120)
    return user_score


main()