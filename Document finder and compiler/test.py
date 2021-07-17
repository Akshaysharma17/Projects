import traceback
import PySimpleGUI as sg

layout = [  [sg.Text('My Window')],
            [sg.Input(key='-IN-'), sg.Text(size=(12,1), key='-OUT-')],
            [sg.Button('Go'), sg.Button('Exit')]  ]

window = sg.Window('Window Title', layout)

try:
    while True:             # Event Loop
        event, values = window.read()
        window.bad()
        print(event, values)
        if event in (None, 'Exit'):
            break
        if event == 'Go':
            window['-OUT-'].update(values['-IN-'])
    window.close()
except Exception as e:
    tb = traceback.format_exc()
    sg.Print(f'An error happened.  Here is the info:', e, tb)
    sg.popup_error(f'AN EXCEPTION OCCURRED!', e, tb)