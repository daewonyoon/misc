# std
import os
import threading

# 3rd
import PySimpleGUI as sg
import pytube


sg.change_look_and_feel("Material2")

EVT_PROGRESS = "-EVENT_PROGRESS-"

layout = [
    [sg.Text("copy youtube url below :"), sg.Text(size=(25, 1), key="-OUTPUT-")],
    [sg.Text("youtube url", size=(10, 1)), sg.Input(key="-URL-")],
    [sg.Text("save folder", size=(10, 1)), sg.Input(key="-DIR-"), sg.FolderBrowse()],
    [sg.ProgressBar(100, orientation="h", size=(50, 20), key="-PROGRESS-")],
    [sg.Button("Save"), sg.Button("Exit")],
]


window = sg.Window("Youtube Downloader", layout)


def update_progress(stream, _chunk, bytes_remaining):
    filesize = stream.filesize
    prog_msg = f"{100*(filesize-bytes_remaining)/filesize:0.3f} % 다운로드. "
    prog_msg2 = f"{bytes_remaining//1000} KB ({100*bytes_remaining/filesize:0.3f} %) 남았음."

    print(prog_msg, prog_msg2)
    window["-OUTPUT-"].update(prog_msg2)
    count = 100 * (filesize - bytes_remaining) // filesize
    window["-PROGRESS-"].update(current_count=count, max=100)
    return


def saving_done(_stream, file_path):

    print(f"파일저장 완료. {file_path}")
    window["-OUTPUT-"].update(f"파일저장 완료. {file_path}")
    window["-PROGRESS-"].update(current_count=100, max=100)

    if not os.path.exists(file_path):
        print(f"파일저장 실패. {file_path}")
        window["-OUTPUT-"].update(f"파일저장 실패. {file_path}")

    return


def popup_choose_stream(vids):
    vids = [str(e) for e in vids]
    selected_id = 0
    layout = [
        [sg.Listbox(vids, size=(150, 15), enable_events=True, key="-LIST-")],
        [sg.Button("OK"), sg.Button("Cancel")],
    ]
    win = sg.Window("Select Stream", layout)
    while True:
        event, values = win.read()
        if event in (sg.WIN_CLOSED, "OK", "Cancel"):
            break
        if event == "-LIST-" and len(values["-LIST-"]):
            selected = values["-LIST-"][0]
            selected_id = vids.index(selected)
            print("seletected : ", selected, selected_id)
    win.close()
    return selected_id


def save_youtube(url, folder):
    print("url:", url)
    print("folder:", folder)
    if len(folder) == 0:
        folder = os.getcwd()

    yt = pytube.YouTube(url)
    yt.register_on_progress_callback(update_progress)
    yt.register_on_complete_callback(saving_done)

    vids = yt.streams

    l = []
    for i, v in enumerate(vids):
        l.append("%3d : %s" % (i, v))
        print(l[-1])

    i = popup_choose_stream(vids)

    thread_download = lambda: vids[i].download(folder)
    threading.Thread(target=thread_download, daemon=True).start()

    return


while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (None, "Exit"):
        break
    if event == "Save":
        url = values["-URL-"]
        folder = values["-DIR-"]
        window["-OUTPUT-"].update("saving...")
        save_youtube(url, folder)


window.close()
