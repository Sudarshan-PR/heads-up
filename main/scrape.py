from bs4 import BeautifulSoup
import requests

class ScrapeAmzn:
    def __init__(self, link):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
        self.url = link
        self.page = requests.get(self.url, headers=self.headers)


    def getPrice(self):
        soup = BeautifulSoup(self.page.content, "lxml")

        if(str(soup.find(id='priceblock_ourprice')) == "None"):
            data = soup.find(id='priceblock_dealprice').get_text()
        else:
            data = soup.find(id='priceblock_ourprice').get_text()

        price = ''.join(i for i in data if i.isdigit())

        price = int(price)
        price /= 100

        return price

#-----object creation example
#----------scrap = scrapAmzn("https://www.amazon.in/Reno2-Storage-Additional-Exchange-Offers/dp/B07XBYF7DL")
#----------scrap.getPrice()