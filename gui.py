#!/usr/bin/env python3

import PySimpleGUI as sg

names = ['Roberta', 'Richi', 'Kylie', 'Jenny', 'Helen',
        'Andrea', 'Meredith', 'Deborah', 'Pauline',
        'Belinda', 'Wendy']

layout_first_column = [
                      [ sg.Text('Nome del cliente') ],
                      [ sg.Input(size=(20, 1), enable_events=True, key='-INPUT-') ],
                      [ sg.Listbox(names, size=(20, 20), enable_events=True, key='-LIST-') ]
                      ]

num_row = 20
num_col = 4

header_list  = ['Qualità','Collo','Qt','Prezzo Unitario','Prezzo Totale']
layout_table = [[sg.Text(str(i), size=(4, 1), justification='right')] + [sg.Input(size=(20, 1), pad=(1, 1), justification='right', key=(i, j)) for j in range(num_col)] for i in range(num_row)]


layout = [[sg.Column(layout_first_column),
           sg.Text('Nome_prova', key='-CLIENT_NAME-'),
           sg.Column(layout_table, size=(800, 600), scrollable=True)]]

window = sg.Window('LibreWinery GUI', layout, return_keyboard_events=True, resizable=True).Finalize()

current_selection_index = 0
window.Element('-LIST-').Update(set_to_index=current_selection_index)

new_values = names
prec_input = 'MaiDireMai'

# Event Loop
while True:
    event, values = window.read()
    print(event, values)                                # debug
    print('prec_input=',prec_input)
    if event in (sg.WIN_CLOSED, 'Exit'):                # always check for closed window
        break
    if values['-INPUT-'] != '' and values['-INPUT-'] != prec_input:   # if a keystroke entered in search field
        current_selection_index = 0
        search = values['-INPUT-']
        new_values = [x for x in names if search in x]  # do the filtering
        window['-LIST-'].update(new_values)             # display in the listbox
        prec_input = values['-INPUT-']
    if values['-INPUT-'] == '':
        # display original unfiltered list
        window['-LIST-'].update(names)
    if 'Up' in event:
        current_selection_index = (current_selection_index - 1) % len(new_values)
    if 'Down' in event:
        current_selection_index = (current_selection_index + 1) % len(new_values)
    if event == '\r':
        print(values['-LIST-'])             # debug
        window.Element('-CLIENT_NAME-').Update(new_values[current_selection_index])
    if event in ('Tab:23', '-LIST-'):
        pass
    
    print(current_selection_index)
    window.Element('-LIST-').Update(set_to_index=current_selection_index)
    window.Element('-CLIENT_NAME-').Update(new_values[current_selection_index])

window.close()

