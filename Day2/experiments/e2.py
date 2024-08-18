# while True:
#     print("hello")

user_prompt = 'Enter a todo: '

todos = []

while True:
    todo = input(user_prompt)
    # print(todo.capitalize())
    print(todo.title())
    todos.append(todo)