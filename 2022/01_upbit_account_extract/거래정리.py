from upbit.client import Upbit as Ubt
import pyupbit
import pandas as pd
import numpy as np
import datetime as dt
# pd.options.display.float_format = '{:.5f}'.format

# 다음의 모듈이 설치되어 있어야 합니다.
# numpy pandas pyupbit upbit-client openpyxl 만약 모듈이 설치되어 있지 않다면 설치를...
# pip install numpy pandas pyupbit upbit-client openpyxl 

access_key = '본인의 업비트access_key'
secret_key = '본인의 업비트secret_key'

# with open('API.ini', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     access_key = lines[0].strip()
#     secret_key = lines[1].strip()

def 거래내역리스트(market = None, state = 'done', cnt = 3):
    pd.options.display.float_format = '{:.0f}'.format
    ubt = Ubt(access_key, secret_key)
    dfs = []
    if market == None:
        tickers = pyupbit.get_tickers('KRW')
    if market != None:
        tickers = market
        
    for ticker in tickers:
        for cnt in range(1, cnt + 1):
            res = ubt.Order.Order_info_all(market=ticker, state = state, page = cnt)
            if len(res['result']) > 0:
                df = pd.DataFrame(res['result'])
                dfs.append(df)
    dfs = pd.concat(dfs)
    
    df = dfs.copy()
    df['created_at'] = pd.to_datetime(df['created_at']).dt.tz_localize(None)
    df = df.astype({
        'volume':'float',
        'price':'float',
        'paid_fee':'float',
        'executed_volume':'float'
    })
    df.sort_values('created_at', ascending = False,inplace=True)
    df.rename(columns = {'market': '코인', 'side': '종류', 'price':'거래단가', 'executed_volume':'거래수량', 'paid_fee': '수수료', 'created_at':'주문시간'}, inplace=True)
    df['거래금액'] = df['거래수량'] * df['거래단가']
    df['정산금액'] = np.where(df['종류'] == 'bid', df['거래금액'] + df['수수료'], df['거래금액'] - df['수수료'])
    df['종류'] = df['종류'].apply(lambda x: '매수' if x == 'bid' else '매도')
    df['마켓'] = df['코인'].str.split('-').str[0]
    df['코인'] = df['코인'].str.split('-').str[1]
    df.set_index('주문시간', inplace=True)
    df = df[['코인', '마켓', '종류','거래수량', '거래단가', '수수료', '정산금액']]
    return df

def 거래내역리스트엑셀로():
    거래내역리스트().to_excel(f'{dt.datetime.now().strftime("%Y-%m-%d")}_거래내역리스트.xlsx')
    
def 입출금리스트(kind = None):
    pd.options.display.float_format = '{:.0f}'.format
    ubt = Ubt(access_key, secret_key)
    columns_dict = {'type': '종류', 'uuid': 'uuid', 'currency': '기준화폐', 'txid': '거래증명ID', 'state': '입출금상태', 'created_at': '생성시간', 'done_at': '거래완료시간',
        'amount': '거래금액', 'fee': '수수료', 'transaction_type': '입금유형'}
    dep = ubt.Deposit.Deposit_info_all()
    wit = ubt.Withdraw.Withdraw_info_all()
    dep_row = pd.DataFrame(dep['result'], columns = list(columns_dict.keys())).rename(columns = columns_dict)
    wit_row = pd.DataFrame(wit['result'], columns = list(columns_dict.keys())).rename(columns = columns_dict)
    df_row = pd.concat([dep_row,wit_row])
    df_row['종류'] = df_row['종류'].apply(lambda x: '입금' if x == 'deposit' \
                                                            else ('출금' if x == 'withdraw' else x))
    df_row['입출금상태'] = df_row['입출금상태'].apply(lambda x: '처리중' if x == 'SUBMITTING' \
                                                            else ('처리완료' if x == 'SUBMITTED' \
                                                            else ('입출금 대기중' if x == 'ALMOST_ACCEPTED' \
                                                            else ('거절' if x == 'REJECTED' \
                                                            else ('승인완료' if x == 'ACCEPTED' or x == 'DONE'\
                                                            else ('처리중' if x == 'PROCESSING' \
                                                            else ('취소됨' if x == 'CANCELED' \
                                                            else ('실패' if x == 'FAILED' \
                                                            else x))))))))
    df_row['입금유형'] = df_row['입금유형'].apply(lambda x: '일반입금' if x == 'default' \
                                                        else ('바로입금' if x == 'internal' else x))
    df_row['거래완료시간'] = pd.to_datetime(df_row['거래완료시간']).dt.tz_localize(None)
    df_row['생성시간'] = pd.to_datetime(df_row['생성시간']).dt.tz_localize(None)
    df_row = df_row.astype({'거래금액':'float', '수수료':'float'})
    df_row['정산금액'] = df_row['거래금액'] + df_row['수수료']
    df_row.dropna(inplace=True)
    df_row = df_row[['거래완료시간', '종류', '거래금액', '수수료', '정산금액', '입출금상태', '기준화폐', 'uuid', '거래증명ID', '생성시간', '입금유형']].set_index('거래완료시간').sort_index(ascending = False)
    # df_row.set_index('거래완료시간').sort_index(ascending = False)
    df = df_row[['종류', '거래금액', '수수료', '정산금액', '입출금상태', '입금유형', '기준화폐']]
    if kind == None:
        return df
    elif kind == 'row':
        return df_row
    
def 입출금리스트엑셀로():
    입출금리스트().to_excel(f'{dt.datetime.now().strftime("%Y-%m-%d")}_입출금리스트.xlsx')
def 누적입출금현황():
    df = 입출금리스트()
    입금총액 = df.loc[df['종류'] == '입금', '정산금액'].sum()
    출금총액 = df.loc[df['종류'] == '출금', '정산금액'].sum()
    return print(f'입금 총액({입금총액}) - 출금 총액({출금총액}) = {입금총액 - 출금총액}')    

# 거래내역 = 거래내역리스트()
# print(거래내역)
# 입출금 = 입출금리스트()
# print(입출금)

거래내역리스트엑셀로()
입출금리스트엑셀로()
누적입출금현황()