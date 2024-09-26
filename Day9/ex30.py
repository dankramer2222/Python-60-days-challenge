# Write a program that:
#
# 1. asks users to enter a password.
#
# 2. returns "Great password there" if the password has more than 7 characters.
#
# 3. returns "Password is OK, but not too strong" if the password has exactly 7 characters.
#
# 4. returns "Your password is weak" if the password has 7 or fewer characters.

user_password = input("Enter a new password: ")
if len(user_password) < 7:
    print("Your password is weak.")
elif len(user_password) == 7:
    print("Password is OK, but not too strong")
else:
    print('Great password there!')