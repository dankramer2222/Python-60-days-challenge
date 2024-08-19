waiting_list = ['John', 'Sen', 'Lisa']
# waiting_list.sort()
waiting_list.sort(reverse=True)
for index, item in enumerate(waiting_list):
    print(f"{index + 1}.{item.capitalize()}")