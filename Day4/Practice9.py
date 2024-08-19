# Create a program that:
#
# 1. Prompts the user to input a (dollar) amount.
#
# 2. Calculates the corresponding amount in euros, given an exchange rate of 2.
#
# 3. Prints out the amount in euros.


dollar_amount = float(input("Enter the amount in dollars: "))

exchange_rate = 2
euro_amount = dollar_amount / exchange_rate

print(f"The equivalent amount in euros is: {euro_amount}")
