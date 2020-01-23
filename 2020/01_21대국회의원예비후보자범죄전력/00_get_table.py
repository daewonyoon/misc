import pandas as pd


url = 'http://tamsak.kbs.co.kr/candidate_info.php'
dfs = pd.read_html(url)
df = dfs[0]
df.to_csv('21대국회의원예비후보자범죄전력.csv', index=False)