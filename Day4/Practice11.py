# We have defined the same ranking list as in the previous exercise:
#
# This time you should create a program that:
#
# 1. Contains the above list.
#
# 2 Prompts the user to input the person's name.
#
# 3. Returns the rank that person has.
#
ranking = ['John', 'Sen', 'Lisa']

name = input("Enter a name: ").capitalize()

if name in ranking:
    rank = ranking.index(name) + 1  # Add 1 because list indices start at 0
    print(f"{name} is ranked {rank}.")
else:
    print(f"{name} is not in the ranking list.")