import csv
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus


# 네이버 모바일 웹에서 view 검색 결과 가져오기(pc와 좀 다름)

# api_txt_lines total_tit

search = input('검색어 입력: ')
url = f'https://m.search.naver.com/search.naver?where=m_view&sm=mtb_jum&query={quote_plus(search)}'
html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

total = soup.select('.api_txt_lines.total_tit')
search_list = []

for i in total:
    temp = []
    temp.append(i.text)
    temp.append(i.attrs['href'])
    search_list.append(temp)

# newline: 한 줄 추가하기 위해 사용
f = open(f'{search}.csv', 'w', encoding='utf-8', newline='')
csv_writer = csv.writer(f)
for i in search_list:
    csv_writer.writerow(i)

f.close()
print('complete')