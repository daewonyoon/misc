from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

import random


class Bible:
    def __init__(self):
        self.bible_list = self.get_bible()

    def get_bible(self):
        file_name = "개역한글판성경.txt"
        with open(file_name, "r", encoding="cp949") as f:
            bible_list = [line for line in f.readlines()]
        return bible_list

    def choose_one(self):
        return random.choice(self.bible_list)


class MyWindow(Tk):
    def __init__(self):
        super().__init__()

        ttk.Style().theme_use("clam")
        self.bible = Bible()

        self.title("Today's Word")
        self.geometry("700x180")
        self.configure(padx=10, pady=10)
        self.resizable(False, False)

        self.label = ttk.Label(self, text="버튼을 눌러, 오늘의 말씀을 뽑으세요.", wraplength=650, relief="sunken")
        self.label.configure(borderwidth=5, font="{맑은 고딕} 12 {}", padding=5)
        self.label.pack(fill="both", ipadx=5, ipady=5, side="top")

        self.button = ttk.Button(self, text="말씀뽑기", command=self.clicked)
        self.button.pack(anchor="sw", side="bottom")

    def clicked(self):
        self.label.configure(text=self.bible.choose_one())


"""
def main_():
    win = Tk()
    ttk.Style().theme_use("clam")
    bible = Bible()

    win.title("Today's Word")
    lbl = Label(win, text="버튼을 눌러, 오늘의 말씀을 뽑으세요.", wraplength=600, justify="left", relief="sunken")
    lbl.grid(column=0, row=0, ipadx=10, ipady=10, padx=10, pady=10)

    def clicked():
        lbl.configure(text=bible.choose_one())

    btn = Button(win, text="말씀뽑기", command=clicked)
    btn.grid(column=0, row=1, sticky="sw", ipadx=10, ipady=10, padx=10, pady=10)

    win.mainloop()
"""


def main():
    win = MyWindow()
    win.mainloop()


if __name__ == "__main__":
    main()
