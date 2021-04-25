"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

states_dict = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
# print(states_dict)

# state_code = input("Enter short state: ").upper()
# while state_code != "":
#     if state_code in states_dict:
#         print(state_code, "is", states_dict[state_code])
#     else:
#         print("Invalid short state")
#     state_code = input("Enter short state: ").upper()
# for loop
for state in states_dict:
    state_name = states_dict[state]
    print("{} is {}".format(state, state_name))
