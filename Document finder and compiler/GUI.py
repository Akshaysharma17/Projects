from traceback import clear_frames
import PySimpleGUI as sg
sg.change_look_and_feel('Dark')
class Gui:
    def __init__(self):
        self.layout=[[sg.Text('Search Term',size=(10,1)),
                      sg.Input(size=(45,1),focus=True,key='TERM'),
                      sg.Radio('Contains',group_id='choice',key='CONTAINS'),
                      sg.Radio('Starts with',group_id='choice',key='STARTSWITH'),
                      sg.Radio('Ends with',group_id='choice',key='ENDSWITH')],

                     [sg.Text('Root Path',size=(10,1)),
                      sg.Input(size=(45,1),key='PATH'),
                      sg.FolderBrowse('Browse'),
                      sg.Button('Re-Index',size=(10,1),key='_INDEX_'),
                      sg.Button('Search',size=(10,1),bind_return_key=True,key='_SEARCH_')],
                     [sg.Output(size=(100,30),key='_OUTPUT_')]]
        self.window= sg.Window('File Search Engine').layout(self.layout)