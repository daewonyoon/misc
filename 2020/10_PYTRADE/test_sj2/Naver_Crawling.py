import requests
from bs4 import BeautifulSoup
import pandas
import datetime
import os
import time

# 네이버에서 해당 종목의 종가 시가 고가 저가 거래량을 가져오는 코드임 ...
# 인터넷에서 csv로 데이터를 저장하는 의미가 있음. ..
def 네이버수정종가크롤링(코드, 년수):

    현재디렉토리 = os.getcwd()
    print("현재 디렉토리:%s" % 현재디렉토리)
    오늘날짜 = datetime.datetime.now()  # 현재 날짜 가져오기
    기간 = float(년수) * 365
    가져올_기간 = float(기간) / 1.47  # 366일 = 248 (1년 기준)
    네이버주소 = f"https://fchart.stock.naver.com/sise.nhn?symbol={코드}&timeframe=day&count={가져올_기간}&requestType=0"
    request_result = requests.get(네이버주소)
    bs = BeautifulSoup(request_result.content, "html.parser")
    ##<protocol>
    ##<chartdata symbol="005930" name="삼성전자" count="5000" timeframe="day" precision="0" origintime="19900103">
    ##<item data="20000810|6000|6160|5860|6160|816612"/>
    ##</chartdata>
    ##</protocol>
    all_data = bs.select("chartdata")
    종목명 = all_data[0].attrs["name"]

    # 종목명과 연관된 디렉토리를 만든다.
    작업디렉토리 = f"{현재디렉토리}\{str(코드)}-{str(종목명)}"
    if (os.path.exists(작업디렉토리)) == False:
        os.mkdir(작업디렉토리)
    # 디렉토리를 작업으로 이동시킨다.
    os.chdir(작업디렉토리)

    주가데이터 = bs.select("item")
    데이터_dict = {}
    날짜_dict = {}
    행번호_list = []
    날짜_list = []
    수정종가_list = []
    전일비_list = []
    시가_list = []
    고가_list = []
    저가_list = []
    거래량_list = []
    거래대금_list = []
    전일비_list = []
    이전종가 = 0
    현재년 = "test"
    과거년 = "test"
    for i in range(len(주가데이터)):
        int_my = str(주가데이터[i])[12:-9]
        int_sptiled = int_my.split("|")
        날짜 = pandas.to_datetime(int_sptiled[0])
        현재년 = str(int_sptiled[0])[0:4]
        if 과거년 == "test":
            과거년 = 현재년
        # 년이 바뀔때 저장하는 곳
        if 현재년 != 과거년:
            날짜_dict["day"] = 날짜_list
            df = pandas.DataFrame(날짜_dict, index=행번호_list)
            df.loc[:, "종가"] = pandas.Series(수정종가_list, index=df.index)
            df.loc[:, "시가"] = pandas.Series(시가_list, index=df.index)
            df.loc[:, "고가"] = pandas.Series(고가_list, index=df.index)
            df.loc[:, "저가"] = pandas.Series(저가_list, index=df.index)
            df.loc[:, "거래량"] = pandas.Series(거래량_list, index=df.index)
            df.loc[:, "거래대금-백만원"] = pandas.Series(거래대금_list, index=df.index)
            df.loc[:, "전일비"] = pandas.Series(전일비_list, index=df.index)
            file_name = f"{코드}-{과거년}-{종목명}"  # 종료지점하고는 과거년이 다르다. ..
            df.index.name = "일련번호"
            df.to_csv("{0}.xlsx".format(file_name))
            print("\n{0} 저장완료".format(file_name))
            과거년 = 현재년
            날짜_list.clear()
            행번호_list.clear()
            수정종가_list.clear()
            시가_list.clear()
            고가_list.clear()
            저가_list.clear()
            거래량_list.clear()
            거래대금_list.clear()
            전일비_list.clear()
        수정종가 = int(int_sptiled[4])
        날짜_list.append(날짜)
        행번호_list.append(i)
        수정종가_list.append(수정종가)
        시가 = int(int_sptiled[1])
        고가 = int(int_sptiled[2])
        저가 = int(int_sptiled[3])
        거래량 = int(int_sptiled[5])
        거래대금 = int((float(거래량) * float(고가)) / float(1000000))
        전일비_list.append(int((float(수정종가) - float(이전종가))))
        이전종가 = int(수정종가)
        시가_list.append(시가)
        고가_list.append(고가)
        저가_list.append(저가)
        거래량_list.append(거래량)
        거래대금_list.append(거래대금)

    # 마지막에 항상 저장하는 곳
    날짜_dict["day"] = 날짜_list
    df = pandas.DataFrame(날짜_dict, index=행번호_list)
    df.loc[:, "종가"] = pandas.Series(수정종가_list, index=df.index)
    df.loc[:, "시가"] = pandas.Series(시가_list, index=df.index)
    df.loc[:, "고가"] = pandas.Series(고가_list, index=df.index)
    df.loc[:, "저가"] = pandas.Series(저가_list, index=df.index)
    df.loc[:, "거래량"] = pandas.Series(거래량_list, index=df.index)
    df.loc[:, "거래대금-백만원"] = pandas.Series(거래대금_list, index=df.index)
    df.loc[:, "전일비"] = pandas.Series(전일비_list, index=df.index)
    file_name = f"{코드}-{현재년}-{종목명}"
    df.index.name = "일련번호"
    df.to_csv("{0}.xlsx".format(file_name))
    print("\n{0} 저장완료".format(file_name))
    os.chdir(현재디렉토리)


# 미사용
def raw_etf_concat(raw_file, etf_file):  # 이전 데이터 파일과 최신 파일 합치는 함수
    raw_file.index = pandas.to_datetime(raw_file.index)  # index를 날짜 포맷으로 변경
    etf_file.index = pandas.to_datetime(etf_file.index)
    # print(etf_file)
    start_day = etf_file.index[0]  # ETF 시작 날짜
    # print(start_day)
    raw_value = raw_file[start_day]
    etf_value = etf_file[start_day]
    amount = etf_value / float(raw_value)
    # print(amount)
    amount_raw = raw_file[: start_day - datetime.timedelta(days=1)] * amount
    # print(amount_raw.tail(20))
    # print(pandas.concat([amount_raw, etf_file]))
    return pandas.concat([amount_raw, etf_file])


# 미사용
def etf_update(코드):
    년수 = 10  # 임의로 설정, 과거 데이터가 10년 전 데이터 경우 변경
    오늘날짜 = datetime.datetime.now()  # 현재 날짜 가져오기
    기간 = float(년수) * 365
    가져올_기간 = 기간 / 1.47  # 366일 = 248 (1년 기준)

    네이버주소 = f"https://fchart.stock.naver.com/sise.nhn?symbol={코드}&timeframe=day&count={가져올_기간}&requestType=0"
    request_result = requests.get(네이버주소)
    bs = BeautifulSoup(request_result.content, "html.parser")
    all_data = bs.select("chartdata")

    종목명 = all_data[0].attrs["name"]
    print(종목명)

    주가데이터 = bs.select("item")
    데이터_dict = {}
    날짜_list = []
    수정종가_list = []
    for i in range(len(주가데이터)):
        int = str(주가데이터[i])[12:-9]
        int_sptiled = int.split("|")
        날짜 = pandas.to_datetime(int_sptiled[0])
        수정종가 = float(int_sptiled[4])
        날짜_list.append(날짜)
        수정종가_list.append(수정종가)
    데이터_dict["Price"] = 수정종가_list

    df = pandas.DataFrame(데이터_dict, index=날짜_list)
    index_fill = pandas.date_range(df.index[0], df.index[-1])
    df = df.reindex(index_fill, method="ffill")
    # print(df['Price'])

    원본_df = read_csv(f"{종목명}")  # 종목명과 동일한 이름의 원본 파일 로드
    합칠_series = 원본_df[원본_df.columns[0]]
    최종파일 = raw_etf_concat(합칠_series, df["Price"])  # raw_etf_concat 함수사용
    # print(최종파일)
    df = pandas.DataFrame(최종파일)
    return_val = df.pct_change() + 1  # 리턴 값 구하기
    concat = pandas.concat([df, return_val], axis=1)
    concat.columns = ["Price", "RETURN"]
    print(concat)
    concat.to_csv("{0}.csv".format(f"{종목명}"), encoding="ms949")
    print("\n{0} 저장완료".format(f"{str(오늘날짜)[:10]}_{종목명}"))


def 전종목크롤링(파일이름, 년수):
    df = pandas.read_excel(파일이름, engine="openpyxl")
    codeSeries = df["종목코드"]
    for 코드 in codeSeries:
        문자코드 = "%06d" % 코드
        print("{0} reading started".format(코드))
        네이버수정종가크롤링(문자코드, 년수)
        print("{0} reading finished".format(코드))
        time.sleep(0.1)


전종목크롤링("전종목코드.xlsx", 10)
# 네이버수정종가크롤링('005930', '1')
# etf_update('069500') # KODEX 200 코드
