# std
import json
import os
import requests
import time
from xml.etree import ElementTree


# 3rd
import pandas as pd
import PySimpleGUI as sg

import xmltodict

# import nlgokr as qngine

# Test this command in a dos window if you are having trouble.
HOW_DO_I_COMMAND = "python -m howdoi.howdoi -n 2"

# if you want an icon on your taskbar for this gui, then change this line of code to point to the ICO file
DEFAULT_ICON = "E:\\TheRealMyDocs\\Icons\\QuestionMark.ico"


sg.theme("Material")


def HowDoI():
    """
    Make and show a window (PySimpleGUI form) that takes user input and sends to the HowDoI web oracle
    Excellent example of 2 GUI concepts
        1. Output Element that will show text in a scrolled window
        2. Non-Window-Closing Buttons - These buttons will cause the form to return with the form's
            values, but doesn't close the form
    :return: never returns
    """

    form = sg.FlexForm("nl.go.kr 도서검색 프로그램", auto_size_text=True, default_element_size=(30, 2), icon=DEFAULT_ICON)
    layout = [
        [sg.Text("검색결과", size=(60, 1))],
        [sg.Output(size=(88, 20))],
        [
            sg.Spin(values=(1, 2, 3, 4), initial_value=1, size=(2, 1), key="Num Answers"),
            sg.T("Num Answers"),
            sg.Checkbox("Display Full Text", key="full text"),
        ],
        [
            sg.Multiline(size=(85, 5), enter_submits=True, key="query"),
            sg.ReadFormButton("검색", bind_return_key=True),
            sg.SimpleButton("나가기"),
        ],
        [sg.Multiline(size=(85, 2), key="rec_key"), sg.SimpleButton("검색2")],
    ]
    form.Layout(layout)
    # ---===--- Loop taking in user input and using it to query HowDoI --- #
    while True:
        (button, value) = form.Read()

        if button == "검색":
            QueryHowDoI(
                value["query"], value["Num Answers"], value["full text"]
            )  # send string without carriage return on end
        elif button == "검색2":
            Query2(value["rec_key"])
        else:
            break  # exit button clicked

    exit(69)


def QueryHowDoI(Query, num_answers, full_text):
    """
    Kicks off a subprocess to send the 'Query' to HowDoI
    Prints the result, which in this program will route to a gooeyGUI window
    :param Query: text english question to ask the HowDoI web engine
    :return: nothing
    """
    output = search_book(Query)
    print("You asked: " + Query)
    print("_______________________________________")
    print(output)
    exit_code = 3


def Query2(rec_key):
    output = search_record(rec_key)
    print(output)
    exit_code = 3


QUERY_URL = "https://nl.go.kr/kolisnet/openApi/open.php"


def search_book(keyword="황순원"):
    """[summary]

    Keyword Arguments:
        keyword {str} -- keyword for book search (default: {"황순원"})

    Returns:
        {str} -- search result in plain txt.
    """

    query = {
        "page": str(1),  # 1페이지
        "per_page": str(20),
        "collection_set": 1,  # 1 단행본
        "sort_ksj": "SORT_TITLE ASC",  # 타이틀 정렬
        "search_field1": "total_field",  # "total_field", "title", "author", "publisher"
        "value1": keyword,  # 검색어1
        # "per_page": 100,
    }
    try:
        r = requests.get(QUERY_URL, params=query)
    except Exception as err:
        print(type(err))
        print(err)
        r = requests.get(QUERY_URL, params=query, verify=False)
    # print(r)
    # print(r.text)
    parse_xml_to_dataframe(r.text, keyword)
    tree = ElementTree.fromstring(r.content)
    # print(xml_tree_stringfy(tree))
    return xml_tree_stringfy(tree)


def search_record(rec_key, word=""):
    query = {"rec_key": rec_key}

    try:
        r = requests.get(QUERY_URL, params=query)
    except Exception as err:
        print(type(err))
        print(err)
        r = requests.get(QUERY_URL, params=query, verify=False)

    d = xmltodict.parse(r.text)

    if d["METADATA"].get("SUCCESS", False):
        return r.text

    # parse_xml_to_dataframe(r.text, rec_key)

    if not os.path.exists(f"./out/{word}/"):
        os.mkdir(f"./out/{word}/")
    with open(f"./out/{word}/result_{word}_{rec_key}.xml", "w", encoding="utf-8") as f:
        f.write(r.text)
    with open(f"./out/{word}/result_{word}_{rec_key}.json", "w", encoding="utf-8") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
    # print(r.content)

    holdinfo_list = d["METADATA"]["HOLDINFO"]
    if type(holdinfo_list) == dict:
        holdinfo_list = [
            holdinfo_list,
        ]

    df = pd.DataFrame(holdinfo_list)
    return r.text


def parse_xml_to_dataframe(request_text, word):
    d = xmltodict.parse(request_text)
    # print(d)
    if d["METADATA"].get("SUCCESS", False):
        print(d)
        return
    df = pd.DataFrame(d["METADATA"]["RECORD"])
    # print(df.to_markdown())

    if not os.path.exists(f"./out/{word}/"):
        os.mkdir(f"./out/{word}/")
    df.to_csv(f"./out/{word}/result_{word}.csv", index=False)
    # data_window(df)
    for idx, row in df.iterrows():
        rec_key = row["REC_KEY"]
        search_record(rec_key, word)
        time.sleep(0.01)


def data_window(df: pd.DataFrame):
    data = df.values.tolist()
    header = df.columns

    lo = [
        [
            sg.Table(
                values=data,
                headings=header,
                display_row_numbers=True,
                auto_size_columns=True,
                num_rows=min(25, len(df)),
            )
        ]
    ]
    w = sg.Window("Result", lo, grab_anywhere=False)
    e, v = w.read()
    w.close()


def xml_tree_stringfy(node, indent="  "):
    """make a string of xml tree structure recursively

    Arguments:
        node {[type]} -- xml node

    Keyword Arguments:
        indent {str} -- indent for tree depth (default: {"  "})
    """

    text = node.text.strip() if node.text else ""
    s = indent + node.tag + " : " + text + "\n"
    for c in node:
        s += xml_tree_stringfy(c, indent + "  ")
    return s


if __name__ == "__main__":
    HowDoI()
