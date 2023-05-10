# need pip install pypi-simple for the below

import PySimpleGUI as sg
from client import simpleGet

layout = [[sg.Text("hello from PySimpleGUI")], [sg.Button("OK")]]

# Create the window
window = sg.Window("Demo", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        simpleGet.printGet()
        break

window.close()