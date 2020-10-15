from pykiwoom.kiwoom import Kiwoom

kw = Kiwoom()
kw.CommConnect(block=True)

kospi = kw.GetCodeListByMarket("0")
kosdaq = kw.GetCodeListByMarket("10")
etf = kw.GetCodeListByMarket("8")

print(len(kospi), kospi)
print(len(kosdaq), kosdaq)
print(len(etf), etf)
