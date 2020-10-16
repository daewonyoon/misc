# std
import datetime
import os
import time

# 3rd
from pykiwoom.kiwoom import Kiwoom


def main():
    # 로그인
    kiwoom = Kiwoom()
    kiwoom.CommConnect()

    # 전종목 종목코드
    kospi = kiwoom.GetCodeListByMarket("0")
    # kosdaq = kiwoom.GetCodeListByMarket("10")
    codes = kospi  # + kosdaq

    # 문자열로 오늘 날짜 얻기
    now = datetime.datetime.now()
    today = now.strftime("%Y%m%d")

    # 전 종목의 일봉 데이터
    for i, code in enumerate(codes):
        if i > 10:
            break
        print(f"{i}/{len(codes)} {code}")
        df = kiwoom.block_request("opt10081", 종목코드=code, 기준일자=today, 수정주가구분=1, output="주식일봉차트조회", next=0)

        dirname = get_dir_path()
        out_name = f"{code}.csv"
        out_path = os.path.join(dirname, out_name)

        df.to_csv(out_path)
        time.sleep(3.5)


def get_dir_path():
    d = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    return os.path.join(d, "dat")


if __name__ == "__main__":
    main()