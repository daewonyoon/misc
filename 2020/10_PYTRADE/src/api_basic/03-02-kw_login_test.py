""" https://wikidocs.net/77481
"""
from pykiwoom.kiwoom import Kiwoom

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)
print("blocking login done")
