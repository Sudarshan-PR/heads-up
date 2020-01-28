from bs4 import BeautifulSoup
import requests

class scrapAmzn:
    def __init__(self, link):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
        self.url = link
        self.page = requests.get(self.url, headers=self.headers)


    def getPrice(self):
        soup = BeautifulSoup(self.page.content, "lxml")

        if(str(soup.find(id='priceblock_ourprice')) == "None"):
            data = soup.find(id='priceblock_dealprice').getText()
        else:
            data = soup.find(id='priceblock_ourprice').getText()

        price = ''.join(i for i in data if i.isdigit())

        price = int(price)
        price /= 100

        #print(price)

        return price

    def getProductName(self):
        soup = BeautifulSoup(self.page.content, "lxml")
        
        name = soup.find(id='productTitle').getText()

        name = name.strip()

        #print(name)

        return name

#-----object creation example
#---------scrap = scrapAmzn("https://www.amazon.in/Nokia-4-2-Black-32GB-Storage/dp/B07RY2NR8F")
#---------scrap.getProductName()
#---------scrap.getPrice()