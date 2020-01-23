import pandas as pd


url = 'http://tamsak.kbs.co.kr/candidate_info.php'
dfs = pd.read_html(url)
df = dfs[0]
df.to_csv('21대국회의원예비후보자범죄전력.csv', index=False)

"""
1. 흉악범죄(살인,강도,성폭력,방화)
2. 폭력범죄(폭행,상해,약취·유인 등)
3. 성매매 및 아동·청소년성보호관련범죄
4. 선거범죄
5. 재산·위조범죄(사기,절도,횡령,배임 등)
6. 풍속범죄(도박,공연음란,마약 등)
7. 교통범죄(무면허,음주운전 등)
8. 공무원범죄(직권남용,뇌물수수 등)
9. 기타범죄
"""