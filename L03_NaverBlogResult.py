import urllib.request
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_='sh_blog_title')
print(title)
print(len(title))
print("===========================================")
title2 = soup.find(class_='sh_blog_title')
print(title2)
print(len(title2))

for i in title:
    print(i.attrs['title'])
    print(i.attrs['href'])
    print()
