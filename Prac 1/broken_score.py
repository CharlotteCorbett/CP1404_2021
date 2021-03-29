"""
CP1404- Practical 1
Charlotte Corbett
Broken program to determine score status
"""
# Fixed program

user_score = float(input("Enter score:"))
if user_score < 0 or user_score == -0 or user_score > 100:
    print("Invalid score")
elif user_score >= 90:
    print("Excellent")
elif user_score >= 50:
    print("Passable")
elif user_score <50:
    print("Bad")
else:
    print("Invalid score")