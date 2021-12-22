# std
import time

# 3rd
import requests
import pandas as pd
from tqdm import tqdm
import xmltodict


def main():

    url = "https://nl.go.kr/kolisnet/openApi/open.php"
    params = {"lib_code": 141001}

    for nnn in (111, 121, 122, 124, 125, 126, 127, 128, 129, 130, 131, 141, 142, 143, 144, 145, 146, 147, 148, 149):

        print(f"---- {nnn} ---")
        libinfos = []

        max_i = nnn * 1000
        for i in tqdm(range(nnn * 1000, (nnn + 1) * 1000)):
            # print(i, end="  ")
            if max_i - i > 50:
                break
            params["lib_code"] = i

            r = requests.get(url, params=params)
            # print(r.text)
            try:
                text = r.text.replace("&", "&amp;")
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
            time.sleep(0.001)

        df = pd.DataFrame(libinfos)
        df.to_csv(f"library_info_{nnn}.csv", index=None)


if __name__ == "__main__":
    main()