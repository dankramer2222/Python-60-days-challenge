user_password = input("Enter a new password: ")
# result = []
result = {}
# if len(user_password) >= 8 and user_password have digit and user_password contain 1 or more upper case letter

if len(user_password) >= 8 and user_password:
    # result.append(True)
    result["length"] = True
else:
    # result.append(False)
    result['length'] = False

digit = False
for i in user_password:
    if i.isdigit():
        digit = True
# result.append(digit)
result["digit"] = digit

upper_case = False
for i in user_password:
    if i.isupper():
        upper_case = True

# result.append(upper_case)
result['upper_case'] = upper_case


if all(result.values()):
    print("Strong password")
else:
    print("You need to work more on your password, please try again")

print(result)
print(result.values())