FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of
    to do items.
    """
    with open(filepath ,'r') as local_file:
        todos_local = local_file.readlines()
    return todos_local

def write_todos(todos_arg,filepath=FILEPATH):
    """ Write a to do item list in a text file."""
    with open(filepath,'w') as local_file:
        local_file.writelines(todos_arg)



