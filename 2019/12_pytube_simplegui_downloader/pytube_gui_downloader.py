import os
import PySimpleGUI as sg
import pytube


sg.change_look_and_feel("Material1")

layout = [
    [sg.Text("copy youtube url below :"), sg.Text(size=(25, 1), key="-OUTPUT-")],
    [sg.Text("youtube url", size=(10, 1)), sg.Input(key="-URL-")],
    [sg.Text("save folder", size=(10, 1)), sg.Input(key="-DIR-"), sg.FolderBrowse()],
    #          [sg.Combo(('',), key='combo1')],
    [sg.Button("Save"), sg.Button("Exit")],
]

window = sg.Window("Youtube Downloader", layout)


# def PopupSelect(lst, title='Select Popup'):
#    sel_idx = 0
#    layout = [[ListBox(values=lst)],
#              [Button('Ok', bind_return_key=True)]]
#
#    return sel_idx
def update_progress(stream, chunk, bytes_remaining):
    filesize = stream.filesize
    prog_msg = f"{100*(filesize-bytes_remaining)/filesize:0.3f} % 다운로드. "
    prog_msg2 = f"{bytes_remaining//1000} KB ({100*bytes_remaining/filesize:0.3f} %) 남았음."

    print(prog_msg, prog_msg2)
    window["-OUTPUT-"].update(prog_msg2)
    return

def saving_done(stream, file_path):
    print(f"파일저장 완료. {file_path}")
    window["-OUTPUT-"].update(f"파일저장 완료. {file_path}")
    return    


def save_youtube(url, folder):
    print("url:", url)
    print("folder:", folder)
    if len(folder) == 0:
        folder = os.getcwd()

    yt = pytube.YouTube(url)
    yt.register_on_progress_callback(update_progress)
    yt.register_on_complete_callback(saving_done)

    vids = yt.streams  # .all()

    l = []
    for i, v in enumerate(vids):
        l.append("%3d : %s" % (i, v))
        print(l[-1])

    text = sg.PopupGetText("\n".join(l), title="Select Video")
    # window['combo1'].Update(values=l)
    i = int(text)

    vids[i].download(folder)
    filename = vids[i].default_filename

    if os.path.exists(os.path.join(folder, filename)):
        return True, vids[i].default_filename
    return False, "unknown error"


while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (None, "Exit"):
        break
    if event == "Save":
        # Update the "output" text element to be the value of "input" element
        url = values["-URL-"]
        folder = values["-DIR-"]
        window["-OUTPUT-"].update("saving...")
        result, msg = save_youtube(url, folder)
        if result:
            result = "File Saved! " + msg
        else:
            result = "Failed. " + msg
        #window["-OUTPUT-"].update(result)


window.close()