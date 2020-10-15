from pprint import pprint

from pykiwoom.kiwoom import Kiwoom

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

login_info_keys = [
    "ACCOUNT_CNT", "ACCNO", "USER_ID", "USER_NAME", "KEY_BSECGB", "FIREW_SECGB"
]

login_info_dic = {
    key: kiwoom.GetLoginInfo(key) for key in login_info_keys
}

print(login_info_dic)
