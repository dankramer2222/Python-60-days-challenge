todos = []

while True:
    user_action = input("type add or show or exit: ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            # print(todos)
            for item in todos:
                print(item)
        case 'exit':
            break
        case _:
            print("yot type not supported command")
