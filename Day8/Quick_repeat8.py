while True:
    user_action = input("Type add , or show/display, or edit,or complete, or exit: ")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("Enter a todo: ") + '\n'

            # file = open("todos.txt", 'r')
            # todos = file.readlines()
            # file.close()

            # * with context manager will be less code and you dont need to close that file after
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            # file = open('todos.txt', 'w')
            # file.writelines(todos)
            # file.close()

            # * same here

            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)

        case "show" | 'display':
            # file = open('todos.txt', 'r')
            # todos = file.readlines()
            # file.close()

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

        #   first method

            # new_todos = []
            # for item in todos:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item)

        #   second method            list comprehension
        #     new_todos = [item.strip('\n') for item in todos]

        #   for index, item in enumerate(todos):
        #     for index, item in enumerate(new_todos):
        #         item = item.title()
        #         print(f"{index+1}.{item}")
            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index+1}.{item}"
                print(row)

        case "edit":
            number = int(input("Enter a number of todo task that you want to edit: "))
            number = number -1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter a new todo")
            todos[number] = new_todo = '\n'

            # existing_todo = todos[number]
            # print(todos[number])

            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)

        case "complete":
            number = int(input("number of the todo that complete: "))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            index_remove = number - 1
            todo_to_remove = todos[index_remove].strip('\n')
            todos.pop(index_remove)

            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)

            message = f'Todo {index_remove} was removed from the list'

        case "exit":
            break
        case _:
            print("hey,you entered an unknown command")
