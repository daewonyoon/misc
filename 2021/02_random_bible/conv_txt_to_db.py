import pandas as pd
import sqlite3
from tqdm import tqdm

book_name_short = [
    "창"
    "출"
    "레"
    "민"
    "신"
    "수"
    "삿"
    "룻"
    "삼상"
    "삼하"
    "왕상"
    "왕하"
    "대상"
    "대하"
    "스"
    "느"
    "에"
    "욥"
    "시"
    "잠"
    "전"
    "아"
    "사"
    "렘"
    "애"
    "겔"
    "단"
    "호"
    "욜"
    "암"
    "옵"
    "욘"
    "미"
    "나"
    "합"
    "습"
    "학"
    "슥"
    "말"
    "마"
    "막"
    "눅"
    "요"
    "행"
    "롬"
    "고전"
    "고후"
    "갈"
    "엡"
    "빌"
    "골"
    "살전"
    "살후"
    "딤전"
    "딤후"
    "딛"
    "몬"
    "히"
    "약"
    "벧전"
    "벧후"
    "요일"
    "요이"
    "요삼"
    "유"
    "계"
]


def read_from_csv():
    with open("개역한글판성경.utf8.txt", "r", encoding="utf-8") as f:
        books = []
        chapters = []
        verses = []
        texts = []
        prev_line = ""
        for line in f.readlines():
            if len(line.strip()) == 0:
                print(prev_line)
                continue
            splitted = line.split()
            if len(splitted) == 0:
                print(prev_line)
                print(line, splitted)
            prev_line = line
            book_ch_verse = splitted[0]
            text = " ".join(splitted[1:])
            idx = 0
            while not line[idx].isnumeric():
                idx += 1
            book = line[:idx]
            ch_verse = book_ch_verse[idx:]
            ch, verse = map(int, ch_verse.split(":"))
            books.append(book)
            chapters.append(ch)
            verses.append(verse)
            texts.append(text)
    return books, chapters, verses, texts


books, chapters, verses, texts = read_from_csv()
df = pd.DataFrame({"book": books, "chapter": chapters, "verse": verses, "text": texts})


def parse_line(line):
    s = line.split()
    # if len(s) == 0:
    #    print(line, len(line), s)

    return s[0]


tqdm.pandas()

# df["book-ch-vers"] = df["org"].progress_apply(parse_line)
# df["text"] =  df["org"].apply(lambda s: " ".join(s.split()[1:]))

print(df[:10].to_markdown())

print(df["book"].unique())

with sqlite3.connect("bible_ko_rev.db") as con:
    df.to_sql("bible", con, index_label="uid", if_exists="replace")
