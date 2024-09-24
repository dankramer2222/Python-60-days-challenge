while True:
    user_action = input("Type add , or show/display, or edit,or complete, or exit: ")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("Enter a todo: ") + '\n'

            file = open("todos.txt",'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case "show" | 'display':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                item = item.title()
                print(f"{index+1}.{item}")

        case "edit":
            number = int(input("Enter a number of todo task that you want to edit: "))
            number = number -1
            new_todo = input("Enter a new todo")
            todos[number] = new_todo
            # existing_todo = todos[number]
            # print(todos[number])
        case "complete":
            number = int(input("number of the todo that complete: "))
            todos.pop(number-1)
        case "exit":
            break
        case _:
            print("hey,you entered an unknown command")
