import functions
import PySimpleGUI as sg

Label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip= "Enter a to do")
add_button = sg.Button("Add")

window=sg.Window("My To-Do App", layout=[[Label], [input_box, add_button]])
window.read()
window.close()
