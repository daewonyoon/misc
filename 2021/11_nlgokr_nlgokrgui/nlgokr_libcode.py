# std
from os import walk
import time

# 3rd
import requests
import pandas as pd
from tqdm import tqdm
import xmltodict


def walkaround_xml_error(text: str):
    walkaround_cases = {
        "&": "&amp;",
        "<-": "&lt;-",
        "<북까페>": "&lt;북까페&gt;",
        "<kys609@hanmail.net>": " kys609@hanmail.net ",
    }
    for k, v in walkaround_cases.items():
        text = text.replace(k, v)
    return text


def main():

    url = "https://nl.go.kr/kolisnet/openApi/open.php"
    params = {"lib_code": 141001}

    for nnn in (147, ):
    #for nnn in (111, 121, 122, 124, 125, 126, 127, 128, 129, 130, 131, 141, 142, 143, 144, 145, 146, 147, 148, 149):

        print(f"---- {nnn} ---")
        libinfos = []

        max_i = nnn * 1000
        for i in tqdm(range(nnn * 1000, (nnn + 1) * 1000)):
            # print(i, end="  ")
            if i - max_i > 50:
                break
            params["lib_code"] = i

            r = requests.get(url, params=params)
            # print(r.text)
            try:
                text = walkaround_xml_error(r.text)

                d = xmltodict.parse(text)

                if d["METADATA"].get("LIBINFO", False):
                    libinfos.append(d["METADATA"]["LIBINFO"])
                    max_i = i
                    # print(libinfos)
                # input()
            except Exception as e:
                print("-" * 20 + f" {i} " + "-" * 20)
                print(e)
                print(r.text)
                with open(f"xml_err_{nnn}_{i}.xml", "w", encoding="utf-8") as f:
                    f.write(r.text)
            time.sleep(0.03)

        df = pd.DataFrame(libinfos)
        df.to_csv(f"./out/library_info_{nnn}.csv", index=None)


if __name__ == "__main__":
    main()