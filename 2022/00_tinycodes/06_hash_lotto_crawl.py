import requests as req
from bs4 import BeautifulSoup as bs
from tqdm import tqdm


print('몇회차부터 몇회차 까지의 번호를 메모장에 저장하고 싶숩니까?')
a,b = map(int, input().split(' '))
with open('lotto_{}_{}.txt'.format(a, b), 'w', encoding='UTF-8') as f:
    for i in tqdm(range(a,b+1)):
        lotto_url = "https://dhlottery.co.kr/gameResult.do?method=byWin"
        lotto_get = req.get(lotto_url, params={"method":"byWin","drwNo":"{}".format(i)})
        spoon = bs(lotto_get.content, 'html.parser')
        get_win_num = []
        get_bonus_num = 0
        for num in spoon.select('.win span'):
            get_win_num.append(num.text)
        for num in spoon.select('.bonus span'):
            get_bonus_num = num.text

        f.write(f"{i},")
        for number in get_win_num:
            f.write(f"{number},")
        f.write(f"{get_bonus_num}")
        f.write('\n')