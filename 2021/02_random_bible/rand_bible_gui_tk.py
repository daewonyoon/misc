from tkinter import *

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


def main():
    win = Tk()
    bible = Bible()

    win.title("Today's Word")
    lbl = Label(win, text="버튼을 눌러, 오늘의 말씀을 뽑으세요.")
    lbl.grid(column=0, row=1)

    def clicked():
        lbl.configure(text=bible.choose_one())

    btn = Button(win, text="말씀뽑기", command=clicked)
    btn.grid(column=1, row=2)

    win.mainloop()


if __name__ == "__main__":
    main()
