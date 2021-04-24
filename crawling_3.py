import bs4
import urllib.request as url

for i in range(4):
    print("Collecting data from page : {}".format(i+1))
    path = 'https://www.flipkart.com/search?q=tv+smart&page={}'.format(i+1)
    res = url.urlopen(path)
    page = bs4.BeautifulSoup(res, 'lxml')
    titles = page.find_all('div',class_='_4rR01T')

    priceList = page.find_all('div', class_='_30jeq3 _1_WHN1')

    for j in range(len(titles)):
        print(titles[j].text)
        print(priceList[j].text)
        print('*' * 50)
