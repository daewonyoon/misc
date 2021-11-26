import PySimpleGUI as sg
import subprocess

import requests
import sys
import time
from xml.etree import ElementTree

# import nlgokr as qngine

# Test this command in a dos window if you are having trouble.
HOW_DO_I_COMMAND = "python -m howdoi.howdoi -n 2"

# if you want an icon on your taskbar for this gui, then change this line of code to point to the ICO file
DEFAULT_ICON = "E:\\TheRealMyDocs\\Icons\\QuestionMark.ico"


def HowDoI():
    """
    Make and show a window (PySimpleGUI form) that takes user input and sends to the HowDoI web oracle
    Excellent example of 2 GUI concepts
        1. Output Element that will show text in a scrolled window
        2. Non-Window-Closing Buttons - These buttons will cause the form to return with the form's
            values, but doesn't close the form
    :return: never returns
    """
    # -------  Make a new FlexForm  ------- #
    # Set system-wide options that will affect all future forms.  Give our form a spiffy look and feel
    sg.SetOptions(
        background_color="#9FB8AD",
        text_element_background_color="#9FB8AD",
        element_background_color="#9FB8AD",
        scrollbar_color=None,
        input_elements_background_color="#F7F3EC",
        button_color=("white", "#475841"),
    )
    form = sg.FlexForm("nl.go.kr 도서검색 프로그램", auto_size_text=True, default_element_size=(30, 2), icon=DEFAULT_ICON)
    layout = [
        [sg.Text("검색결과", size=(40, 1))],
        [sg.Output(size=(88, 20))],
        [
            sg.Spin(values=(1, 2, 3, 4), initial_value=1, size=(2, 1), key="Num Answers"),
            sg.T("Num Answers"),
            sg.Checkbox("Display Full Text", key="full text"),
        ],
        [
            sg.Multiline(size=(85, 5), enter_submits=True, key="query"),
            sg.ReadFormButton("검색", button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),
            sg.SimpleButton("나가기", button_color=(sg.YELLOWS[0], sg.GREENS[0])),
        ],
    ]
    form.Layout(layout)
    # ---===--- Loop taking in user input and using it to query HowDoI --- #
    while True:
        (button, value) = form.Read()

        if button == "검색":
            QueryHowDoI(
                value["query"], value["Num Answers"], value["full text"]
            )  # send string without carriage return on end
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


QUERY_URL = "http://nl.go.kr/kolisnet/openApi/open.php"


def search_book(keyword="황순원"):
    """[summary]

    Keyword Arguments:
        keyword {str} -- keyword for book search (default: {"황순원"})

    Returns:
        {str} -- search result in plain txt.
    """

    query = {
        "page": str(1),
        "per_page": str(1000),
        "collection_set": 1,
        "sort_ksj": "SORT_TITLE ASC",
        "search_field1": "total_field",
        "value1": keyword,
    }
    r = requests.get(QUERY_URL, params=query)
    # print(r)
    # print(r.text)
    tree = ElementTree.fromstring(r.content)
    # print(xml_tree_stringfy(tree))
    return xml_tree_stringfy(tree)


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
