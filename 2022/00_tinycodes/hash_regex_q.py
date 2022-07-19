# 데이터 예시
a = [
'가나다라마바사'
, '2020년 2월 2일 이날은..'
, '145692'
, '이건 몇년 전, 2020년 2월 2일...'
]

# 원하는 결과
a_ = [
'2020년 2월 2일 이날은..'
, '이건 몇년 전, 2020년 2월 2일...'
]

import re

for s in a:
    res = re.search(r"\d{4}년 \d{1,2}월 \d{1,2}일", s)
    if res:
        print(s)


a_filtered = [ s for s in a if re.search(r"\d{4}년 \d{1,2}월 \d{1,2}일", s)]        
print(a_filtered)