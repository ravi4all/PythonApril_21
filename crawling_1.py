import bs4
import urllib.request as url

path = 'https://www.flipkart.com/search?q=tv+smart'
res = url.urlopen(path)
page = bs4.BeautifulSoup(res, 'lxml')
title = page.find('div',class_='_4rR01T')
print(title.text)

price = page.find('div', class_='_30jeq3 _1_WHN1')
print(price.text)
