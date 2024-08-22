import functions
import time

now = time.strftime("%Y-%m-%d %H:%M:%S")
print(f"It is {now}")

while True:
    user_action = input('Type add,show,edit,complete or exit or help:')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todo()

        todos.append(todo + '\n')

        functions.write_todo(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todo()

        for index,item in enumerate(todos):
            item = item.strip('\n')
            row=f"{index+1}--{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number=int(user_action[5:])

            todos = functions.get_todo()
            old_todo = todos[number-1]

            new_todo = input("Enter a new todo:")
            todos[number-1] = new_todo + '\n'

            functions.write_todo(todos)

        except ValueError:
            print("your command is invalid enter index after edit")
            continue
        except IndexError:
            print("your index is out of range")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todo()

            old_todo=todos[number-1]

            msg = f"""Do you really wanna delete the below todo
{number}--{todos[number-1]}y/n:"""
            confirm_msg = input(msg)

            if(confirm_msg == 'y'):
                todos.pop(number-1)
            else:
                continue

            functions.write_todo(todos)

        except ValueError:
            print("invalid command! Enter index after complete")
            continue
        except IndexError:
            print("Index out of range")
            continue

    elif user_action.startswith('exit'):
        break
    elif user_action.startswith('help'):
        cmd1=f"add (todo)"
        cmd2=f"show"
        cmd3=f"edit (index)"
        cmd4= f"complete (index)"
        cmd5=f"exit"
        print("The available commands are:")
        print(f"{cmd1+'\n'}{cmd2+'\n'}{cmd3+'\n'}{cmd4+'\n'}{cmd5+'\n'}")

    else:
        print("invalid command!")



