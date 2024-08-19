# In the coding area, we have defined a country variable.
#
# You should write a match-case block that checks the value of the country variable and:
#
# Prints out Hello if the value of country is "USA".
#
# Prints out Namaste if the value of country is "India".
#
# Prints out Hallo if the value of country is "Germany".

country = "India"

match country:
    case "USA":
        print("Hello")
    case "India":
        print("Namaste")
    case "Germany":
        print("Hallo")
