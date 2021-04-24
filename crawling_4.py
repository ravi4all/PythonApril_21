import bs4
import urllib.request as url

product_name = input("Enter product name : ")
product_name = product_name.replace(' ', '+')
path = 'https://www.flipkart.com/search?q={}'.format(product_name)
res = url.urlopen(path)
page = bs4.BeautifulSoup(res, 'lxml')
titles = page.find_all('div',class_='_4rR01T')
priceList = page.find_all('div', class_='_30jeq3 _1_WHN1')

for i in range(len(titles)):
    print(titles[i].text)
    print(priceList[i].text)
    print('*' * 50)
