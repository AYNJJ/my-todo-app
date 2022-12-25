FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):
    """ Reads a text file and returns the list of
    to do items """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todo_args, filepath=FILEPATH):
    """ Writes to a text file and adds new items """
    with open(filepath, 'w') as file:
        file.writelines(todo_args)