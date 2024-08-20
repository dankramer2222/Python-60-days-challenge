# Extend the given code so it prints out the sum of the numbers.
#
# The output of your code should be as below:
#
# 49.1

user_entries = ['10', '19.1', '20']

sum_entries = [float(i) for i in user_entries]
sum_entries = sum(sum_entries)

print(sum_entries)