while True:
    user_action = input("type add, edit, complete, show, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            # Open the file in read mode to get existing todos
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            # Append the new todo to the list
            todos.append(todo)

            # Write the updated list back to the file
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'edit':
            # Open the file in read mode to get existing todos
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            number = int(input("Number of the todo to edit: "))
            if 0 < number <= len(todos):
                new_todo = input("Enter new todo: ") + "\n"
                todos[number - 1] = new_todo  # Update the specific todo

                # Write the updated list back to the file
                with open('todos.txt', 'w') as file:
                    file.writelines(todos)

                print("This todo has been successfully changed")
            else:
                print("Invalid todo number")

        case 'show':
            # Open the file in read mode to get existing todos
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f'{index + 1} - {item}'
                print(row)

        case 'complete':
            # Open the file in read mode to get existing todos
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            number = int(input("Number of the todo to complete: "))
            if 0 < number <= len(todos):
                todos.pop(number - 1)  # Remove the specified todo

                # Write the updated list back to the file
                with open('todos.txt', 'w') as file:
                    file.writelines(todos)

                print(f"Todo #{number} has been completed and removed.")
            else:
                print("Invalid todo number")

        case 'exit':
            break

        case _:
            print("You typed an unsupported command")
