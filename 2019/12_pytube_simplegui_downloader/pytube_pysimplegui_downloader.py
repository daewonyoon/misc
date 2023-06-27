# std
import os
import threading

# 3rd
import PySimpleGUI as sg
import pytube


sg.change_look_and_feel("Python")

cache_urllast = sg.user_settings_get_entry("-last url-", "")
cache_folderlist = sg.user_settings_get_entry("-savefolders-", [])
cache_folderlast = sg.user_settings_get_entry("-last savefolder-", "")


layout = [
    [sg.Text("copy youtube url below :"), sg.Text(size=(60, 1), key="-OUTPUT-")],
    [sg.Text("youtube url", size=(10, 1)), sg.Input(default_text=cache_urllast, key="-URL-", size=(70, 1))],
    [
        sg.Text("save folder", size=(10, 1)),
        sg.Combo(sorted(cache_folderlist), default_value=cache_folderlast, key="-DIR-", size=(70, 1)),
        sg.FolderBrowse(),
    ],
    [
        sg.ProgressBar(100, orientation="h", size=(40, 20), key="-PROGRESS-"),
        sg.Text(size=(30, 1), key="-PROGRESS_MSG-"),
    ],
    [sg.Button("Save"), sg.Button("Exit")],
]


window = sg.Window("Youtube Downloader", layout, finalize=True)

# save_folder = sg.user_settings_get_entry("-save folder-", "")

# if save_folder:
#    window["-DIR-"].update(save_folder)


def update_progress(stream, _chunk, bytes_remaining):
    """progress bar update callback"""
    filesize = stream.filesize
    bytes_downloaded = filesize - bytes_remaining
    downloaded_percent = 100 * bytes_downloaded / filesize

    prog_msg = f"{downloaded_percent:3.2f}% ({bytes_downloaded//(1024*1024)}MB/{filesize//(1024*1024)}MB)"

    print(prog_msg)
    window["-PROGRESS_MSG-"].update(prog_msg)
    count = int(downloaded_percent)
    window["-PROGRESS-"].update(current_count=count, max=100)
    return


def saving_done(_stream, file_path):
    """progress bar on complete callback"""

    print(f"파일저장 완료. {file_path}")
    # window["-PROGRESS_MSG-"].update("100.00%")
    window["-OUTPUT-"].update(f"파일저장 완료. {file_path}")
    window["-PROGRESS-"].update(current_count=100, max=100)
    window["Save"].update(disabled=False)

    if not os.path.exists(file_path):
        print(f"파일저장 실패. {file_path}")
        window["-OUTPUT-"].update(f"파일저장 실패. {file_path}")

    return


def popup_choose_stream(vids):
    """popup window for choosing stream to save"""
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
    """start saving youtube stream"""
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

    window["-PROGRESS_MSG-"].update("download started.")
    window["Save"].update(disabled=True)
    thread_download = lambda: vids[i].download(folder)
    threading.Thread(target=thread_download, daemon=True).start()

    return


def cache_save_folder_to_settings(folder):
    """program memorizes save folder, even after program ends."""
    cache_save_folders = sg.user_settings_get_entry("-savefolders-", [])
    if folder not in cache_save_folders:
        cache_save_folders.append(folder)
        cache_save_folders.sort()
    # cache_last_save_folder = sg.user_settings_get_entry("-last savefolder-", "")
    sg.user_settings_set_entry("-savefolders-", cache_save_folders)
    sg.user_settings_set_entry("-last savefolder-", folder)


while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (None, "Exit"):
        break
    if event == "Save":
        url = values["-URL-"]
        folder = values["-DIR-"]
        sg.user_settings_set_entry("-last url-", url)
        cache_save_folder_to_settings(folder)
        # sg.user_settings_set_entry("-save folder-", folder)
        window["-OUTPUT-"].update("saving...")
        window["-PROGRESS-"].update(current_count=0, max=100)
        save_youtube(url, folder)


window.close()
