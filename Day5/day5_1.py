todos = []

while True:
    user_action = input("type add, edit, complete, show or exit: ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'edit':
            number = int(input("Number of the todo edit: "))
            number = number - 1
            existing_todo = todos[number]
            newTodo = input("Enter new todo: ")
            todos[number] = newTodo
            print("This todo successfully been changed")
        case 'show':
            # print(todos)
            for index, item in enumerate(todos):
                # print(index, '-', item)
                row = f'{index + 1}-{item}'
                print(row)
        case 'complete':
            number = int(input("number of todo to complete"))
            todos.pop(number - 1)
        case 'exit':
            break
        case _:
            print("yot type not supported command")