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
progressbar = window["-PROGRESS-"]


def update_progress(stream, chunk, bytes_remaining):
    filesize = stream.filesize
    prog_msg = f"{100*(filesize-bytes_remaining)/filesize:0.3f} % 다운로드. "
    prog_msg2 = f"{bytes_remaining//1000} KB ({100*bytes_remaining/filesize:0.3f} %) 남았음."

    print(prog_msg, prog_msg2)
    window["-OUTPUT-"].update(prog_msg2)
    count = 100 * (filesize - bytes_remaining) // filesize
    # progressbar.update(current_count=count, max=100)
    window.write_event_value(EVT_PROGRESS, count)
    return


def saving_done(stream, file_path):

    print(f"파일저장 완료. {file_path}")
    window["-OUTPUT-"].update(f"파일저장 완료. {file_path}")
    progressbar.update(current_count=100, max=100)

    if not os.path.exists(file_path):
        print(f"파일저장 실패. {file_path}")
        window["-OUTPUT-"].update(f"파일저장 실패. {file_path}")

    # window["-PROGRESS-"].UpdateBar(0, 100)
    return


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

    text = sg.PopupGetText("\n".join(l), title="Select Video")
    i = int(text)

    th_download = lambda: vids[i].download(folder)
    threading.Thread(target=th_download, daemon=True).start()

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
    elif event == EVT_PROGRESS:
        print(f"{event}, {values[event]}")
        window["-PROGRESS-"].update(values[event], max=100)


window.close()
