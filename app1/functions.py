FILEPATH = 'todos.txt'


def write_todo(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as local_file:
        local_file.writelines(todos_arg)


def get_todo(filepath=FILEPATH):
    with open(filepath, 'r') as local_file:
        todos = local_file.readlines()
    return todos
