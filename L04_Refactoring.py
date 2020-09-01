import urllib.request
from bs4 import BeautifulSoup
# 한글 검색 가능하도록 필요한 lib
import urllib.parse


baseUrl = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query='
plusUrl = input('검색어를 입력하세요: ')
url = baseUrl + urllib.parse.quote_plus(plusUrl)
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_='sh_blog_title')
# print(title)
print(len(title))

for i in title:
    print(i.attrs['title'])
    print(i.attrs['href'])
    print()
