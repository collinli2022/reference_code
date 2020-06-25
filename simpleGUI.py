""" GUI for pi_pact.py

A bare bones GUI for pi_pact.py written with PySimpleGUI.
"""

import PySimpleGUI as sg
import os

#define empty string for args
args=''

"""
List for window layout. Each line is one row in the window. These elements are later referenced by their keys.
Row 1: Radio Buttons for selection mode
Rows 2-11: Label and text field for their respective args
Row 12: Launch and Cancel Buttons
"""
layout = [
[sg.Text('Mode:', size=[17,1]), sg.Radio('Advertiser', 'ModeSelect', default=True,key='AdRd'), sg.Radio('Scanner', 'ModeSelect', key='ScanRd')],
[sg.Text('Configuration YAML:', size=[17,1]), sg.Input(key='--config_yml')],
[sg.Text('Control File:', size=[17,1]), sg.Input(key='--control_file')],
[sg.Text('Scan File Prefix:', size=[17,1]), sg.Input(key='--scan_prefix')],
[sg.Text('Timeout:', size=[17,1]), sg.Input(key='--timeout')],
[sg.Text('UUID:', size=[17,1]), sg.Input(key='--uuid')],
[sg.Text('Major:', size=[17,1]), sg.Input(key='--major')],
[sg.Text('Minor:', size=[17,1]), sg.Input(key='--minor')],
[sg.Text('Tx Power:', size=[17,1]), sg.Input(key='--tx_power')],
[sg.Text('Interval:', size=[17,1]), sg.Input(key='--interval')],
[sg.Text('Revisit:', size=[17,1]), sg.Input(key='--revisit')],
[sg.Button('Launch', size=[10,1]),sg.Cancel()]]

#Define Window
window=sg.Window('Title',layout)

#Event loop for checking values
while True:
    event, values = window.read()
    #If window is closed or cancel is pressed
    if event in (sg.WIN_CLOSED, 'Cancel'):
        window.close()
        break
    #If launch button is clicked
    if event == 'Launch':
        #Check if Advertiser mode or Scanner mode is selected
        if window['AdRd'].Get():
            args+='-a '
            values.pop('AdRd')
            values.pop('ScanRd')
        elif window['ScanRd'].Get():
            args+='-s'
            values.pop('AdRd')
            values.pop('ScanRd')
        #Check input fields and add argument to command if present
        for item in values.items():
            if item[1]:
                args+='{arg} {argVal} '.format(arg=item[0],argVal=item[1])
        args+='&'
        #Run pi_pact.py with args
        os.system("sudo python3 pi_pact.py {0}".format(args))
        window.close()