import functions
import PySimpleGUI as sg
import  time

sg.theme("Black")
clock_lebel=sg.Text('',key='clock')

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter a todo",key='todo')
add_button = sg.Button(size=2,image_source='add.png',
                       mouseover_colors="LightBlue2",
                       key="Add",tooltip="Add a todo")

complete_button = sg.Button(size=3,image_source='complete.png',
                            mouseover_colors='LightBLue2',
                            key='Complete',tooltip='complete the todo')

#display the todo in a list box

list_box = sg.Listbox(values=functions.get_todo(),
                      key='existing_todo',
                      enable_events=True,size=[45,10])
edit_button = sg.Button("Edit")
exit_button = sg.Button("Exit")

window = sg.Window("My to do list app",
                   layout=[[clock_lebel],
                           [label,input_box,add_button],
                           [list_box,edit_button,complete_button],
                           [exit_button]],
                   font = ('Helvetica',10))

while True:
    event , values = window.read(timeout=100)

    if event == sg.WINDOW_CLOSED or event=='Exit':
        break

    window["clock"].update(value=time.strftime("%Y-%m-%d %H:%M:%S"))

    if event =='Add':
        todos = functions.get_todo()
        new_todo = values["todo"]+"\n"
        todos.append(new_todo)
        functions.write_todo(todos)

        #updating the list box
        window['existing_todo'].update(values=todos)
        window['todo'].update(value='')


    elif event == "Edit":
        try:
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
            window['todo'].update(value='')
        except(IndexError,ValueError):
            sg.popup("plz select an item first and the enter todo in input box")
            continue

    elif event=="existing_todo":
        #on clicking the todo it should appear in text add
        try:
            window['todo'].update(value=values['existing_todo'][0])
        except IndexError:
            continue

    elif event == 'Complete':
        try:
            todo_completed = values['existing_todo'][0]

            todos = functions.get_todo()

            index = todos.index(todo_completed)

            todos.pop(index)
            functions.write_todo(todos)

            #updating the list box and input box
            window['existing_todo'].update(values=todos)
            window['todo'].update(value='')
        except(IndexError,ValueError):
            sg.popup("plz select an item first",font=('Helvetica',15))
            continue






window.close()
