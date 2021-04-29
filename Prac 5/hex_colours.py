COLOURS_DICT = {'antiquewhite1': '#ffefdb', 'antiquewhite2': '#eedfcc', 'antiquewhite3': 'cdc0b0',
                'antiquewhite4': '#8b8378', 'aquamarine1': '#7fffd4', 'aquamarine2': '#76eec6',
                'aquamarine4': '#458b74', 'azure1': '#f0ffff', 'azure2': '#e0eeee', 'azure3': '#c1cdcd'}

print(COLOURS_DICT)
user_colour_choice = input("Colour:")
while user_colour_choice != '':
    try:
        print("{} - {}".format(user_colour_choice, COLOURS_DICT[user_colour_choice]))
    except KeyError:
        print("{} does not exist".format(user_colour_choice))
    user_colour_choice = input("Colour:")

print("Thanks bye")
