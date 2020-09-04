from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from selenium import webdriver

base_url = 'https://www.google.com/search?hl=en&source=hp&ei=p0RSX9uVNsGHoAS756XICA&q='
plus_url = input('검색어 입력: ')
url = base_url + quote_plus(plus_url)

# 같은 폴더에 위치한 'chromedriver' 사용
driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html)

# 클래스 이름이 'r'인 데이터를 가져와서 리스트로 저장
r = soup.select('.r')
for i in r:
    #print(i)
    # select_one이 아닌 select를 하면 텍스트를 가져올 수 없음. 리스트이기 때문
    print(i.select_one('.LC20lb').text)
    print(i.a.attrs['href'])
    print()

driver.close()

# 셀레니움을 사용하는 이유: 셀레니움 없으면 보여지는것과 다른 클래스들을 가지는 데이터를 가져옴.