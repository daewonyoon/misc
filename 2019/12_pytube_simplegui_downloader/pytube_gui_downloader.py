import os
import PySimpleGUI as sg
import pytube


sg.change_look_and_feel('Material1')

layout = [[sg.Text('copy youtube url below :'), sg.Text(size=(25,1), key='-OUTPUT-')],
          [sg.Text('youtube url', size=(10, 1)),sg.Input(key='-URL-')],
          [sg.Text('save folder', size=(10, 1)),sg.Input(key='-DIR-'), sg.FolderBrowse()],
          [sg.Button('Save'), sg.Button('Exit')]]

window = sg.Window('Youtube Downloader', layout)


def save_youtube(url, folder):
    print('url:', url)
    print('folder:', folder)
    if len(folder) == 0:
        folder = os.getcwd()

    yt = pytube.YouTube(url)

    vids = yt.streams.all()
    for i, v in enumerate(vids):
        print('%3d : %s'%(i, v))

    vids[0].download(folder)
    filename = vids[0].default_filename

    if os.path.exists(os.path.join(folder, filename)):
        return True, vids[0].default_filename
    return False, "unknown error"


while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event in  (None, 'Exit'):
        break
    if event == 'Save':
        # Update the "output" text element to be the value of "input" element
        url = values['-URL-']
        folder = values['-DIR-']
        window['-OUTPUT-'].update('saving...')
        result, msg = save_youtube(url, folder)
        if result:
            result = 'File Saved! ' + msg
        else:
            result = 'Failed. ' + msg
        window['-OUTPUT-'].update(result)

window.close()