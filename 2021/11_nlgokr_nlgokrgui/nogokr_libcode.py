import requests
import xmltodict
import pandas as pd


def main():

    for nnn in (111, 121, 131, 141):

        url = "https://nl.go.kr/kolisnet/openApi/open.php"

        params = {"lib_code": 141001}

        libinfos = []

        for i in range(nnn * 1000, (nnn + 1) * 1000):
            print(i, end="  ")
            params["lib_code"] = i

            r = requests.get(url, params=params)
            # print(r.text)
            try:
                text = r.text.replace("&", "&amp;")
                d = xmltodict.parse(text)
                if d["METADATA"].get("LIBINFO", False):
                    libinfos.append(d["METADATA"]["LIBINFO"])
                    # print(libinfos)
                # input()
            except Exception as e:
                print()
                print(e)
                print(r.text)

        df = pd.DataFrame(libinfos)
        df.to_csv(f"library_info_{nnn}.csv", index=None)


if __name__ == "__main__":
    main()