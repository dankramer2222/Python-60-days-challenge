user_date = input("Please enter the date that are current today: ")
user_mood = input('How do you rate your mood today from 1 to 10? ')
user_thoughts = input("let's your thoughts flow:\n")

with open(f"../Day8/Journal/{user_date}.txt", 'w') as file:
    file.write(user_mood + 2 * '\n')
    file.write(user_thoughts)