# std
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from os import walk
import threading
import time

# 3rd
import requests
import pandas as pd
from tqdm import tqdm
import xmltodict

lock = threading.Lock()

def print_locked(s):
    with lock:
        print(s)


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


def query_save_library_info(libcode: int, location: str):

    nnn = libcode
    url = "https://nl.go.kr/kolisnet/openApi/open.php"
    params = {"lib_code": 141001}

    print_locked(f"---- {nnn} ---")
    libinfos = []

    max_i = nnn * 1000
    for i in range(nnn * 1000, (nnn + 1) * 1000):
        if i % 20 == 0:
            print_locked(f"{i} " +  "-" * ((i % 1000) // 20))
        if i - max_i > 50:
            break
        params["lib_code"] = i

        r = requests.get(url, params=params)
        # print_locked(r.text)
        try:
            text = walkaround_xml_error(r.text)

            d = xmltodict.parse(text)

            if d["METADATA"].get("LIBINFO", False):
                libinfos.append(d["METADATA"]["LIBINFO"])
                max_i = i
                # print_locked(libinfos)
            # input()
        except Exception as e:
            print_locked("-" * 20 + f" {i} " + "-" * 20)
            print_locked(e)
            print_locked(r.text)
            with open(f"xml_err_{nnn}_{i}.xml", "w", encoding="utf-8") as f:
                f.write(r.text)
        time.sleep(0.1)

    df = pd.DataFrame(libinfos)
    df.to_csv(f"./out/library_info_{nnn}_{location}.csv", index=None)
    print_locked(f"{location} file written")
    # df.to_csv(f"./out/library_info_{nnn}.csv", index=None)

    return 0


def main():

    # //url = "https://nl.go.kr/kolisnet/openApi/open.php"
    # params = {"lib_code": 141001}
    location_codes = (
        (111, "서울"),
        (121, "부산"),
        (122, "대구"),
        (124, "광주"),
        (125, "대전"),
        (126, "부산"),
        (127, "대구"),
        (128, "인천"),
        (129, "광주"),
        (130, "대전"),
        (131, "울산"),
        (141, "경기"),
        (142, "강원"),
        (143, "충북"),
        (144, "충남"),
        (145, "전북"),
        (146, "전남"),
        (147, "경북"),
        (148, "경남"),
        (149, "제주"),
    )

    with ThreadPoolExecutor(max_workers=5) as exe:
        futures = [exe.submit(query_save_library_info, nnn, loc) for nnn, loc in location_codes]

        for future in as_completed(futures):
            try:
                r = future.result()
                print_locked(f"{future} exits with {r} status")
            except Exception as e:
                print_locked(e)


if __name__ == "__main__":
    main()
