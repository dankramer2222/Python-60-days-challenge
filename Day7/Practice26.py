# Extend the given code so the code prints out a list containing the number of characters for each username.
#
# The output of your code should be as below:
#
# [9, 11, 11]

usernames = ["john 1990", "alberta1970", "magnola2000"]

lengths = []

for i in usernames:
    lengths.append(len(i))
print(lengths)
