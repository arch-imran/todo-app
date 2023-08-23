#from functions import get_todos, write_todos
import functions
import time


now = time.strftime("%b %d %Y  %H:%M:%S")
print("It is ", now)
while True:
    user_action = input ( "Type add, show ,edit,complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        for index,item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number-1

            todos = functions.get_todos('todos.txt')

            new_todo = input("enter a new todo:")
            todos[number] = new_todo +'\n'

            functions.write_todos(todos)

        except ValueError:
            print('Your command is not valid enter index after edit')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos('todos.txt')

            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"todo {todo_to_remove} was removed from the list."
            print(message)

        except (IndexError , ValueError):
            print("OOPs,It seems that either index is out of range or no index after complete ")
            continue

    elif user_action.startswith('exit'):
        print("Bye!")
        break
    else:
        print("OOPS,you entered a wrong command!")




