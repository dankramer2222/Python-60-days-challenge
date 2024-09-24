todos = []

while True:
    user_action = input("Type add , or show/display, or edit, or exit: ")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show" | 'display':
          for item in todos:
              item = item.title()
              print(item)

        case "edit":
            number = int(input("Enter a number of todo task that you want to edit: "))
            number = number -1
            new_todo = input("Enter a new todo")
            todos[number] = new_todo
            # existing_todo = todos[number]
            # print(todos[number])
        case "exit":
            break
        case _:
            print("hey,you entered an unknown command")


print("experiment board -----------------------------------------------")
summer_months = ['June', 'July', 'August']
summer_months[2]