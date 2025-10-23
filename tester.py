import re

password_to_test = input("Enter the password that you want to test: ")

strength_score = 0

if len(password_to_test) >= 12:
    strength_score += 1
    if len(password_to_test) >= 14:
        strength_score += 1


strength_ratings = ["Garbage", "Weak", "Ok", "Good", "Very good!", "Great!", "Amazing!"]
print("Strength score of password: " + strength_ratings[strength_score])
