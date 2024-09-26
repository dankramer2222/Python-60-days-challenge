# Write a program that:
#
# 1. asks users to enter a password.
#
# 2. returns "Great password there!" if the password has more than 7 characters. For example:
# enter a new password mycool_password3001
# Great password there!
#
# 3. returns "Your password is weak." if the password has 7 or fewer characters. For example:
# enter a new password 1234
# your password is weak

user_password = input("Enter a new password: ")
if len(user_password) < 7:
    print("Your password is weak.")
else:
    print('Great password there!')