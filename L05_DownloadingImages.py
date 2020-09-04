from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

base_url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plus_url = input('검색어 입력: ')
# 검색어를 아스키 코드로 변환한 뒤 베이스 url에 붙임
url = base_url + quote_plus(plus_url)
html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# 검색 결과 페이지에서 클래스가 '_img'인 태그들을 가져옴
img = soup.find_all(class_='_img')

n = 1
for i in img:
    img_url = i['data-source']
    with urlopen(img_url) as f:
        with open('./img/' + plus_url + str(n) + '.jpg', 'wb') as h:  # 이미지는 바이너리 파일이므로 w에 b를 붙어야함
            img = f.read()
            h.write(img)
    n += 1
    print(img_url)
print('download complete')
