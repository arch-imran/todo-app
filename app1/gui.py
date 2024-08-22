import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter a todo",key='todo')
add_button = sg.Button("Add")

complete_button = sg.Button("Complete")

#display the todo in a list box

list_box = sg.Listbox(values=functions.get_todo(),
                      key='existing_todo',
                      enable_events=True,size=[45,10])
edit_button = sg.Button("Edit")

window = sg.Window("My to do list app",
                   layout=[[label,input_box,add_button,complete_button],
                           [list_box,edit_button]],
                   font = ('Helvetica',10))

while True:
    event , values = window.read()

    if event =='Add':
        todos = functions.get_todo()
        new_todo = values["todo"]+"\n"
        todos.append(new_todo)
        functions.write_todo(todos)

        #updating the list box
        window['existing_todo'].update(values=todos)


    elif event == "Edit":
        todos = functions.get_todo()

        new_todo = values['todo'] +'\n'
        todo_to_edit = values["existing_todo"][0]
        index = todos.index(todo_to_edit)
        #updating the todo
        todos[index]=new_todo

        #storing todo changed in file
        functions.write_todo(todos)

        #updating the list box
        window['existing_todo'].update(values=todos)

    elif event=="existing_todo":
        #on clicking the todo it should appear in text add
        window['todo'].update(value=values['existing_todo'][0])

    elif event == 'Complete':
        todo_completed = values['existing_todo'][0]

        todos = functions.get_todo()

        index = todos.index(todo_completed)

        todos.pop(index)
        functions.write_todo(todos)

        #updating the list box
        window['existing_todo'].update(values=todos)
    elif event == sg.WINDOW_CLOSED:
        break




window.close()
