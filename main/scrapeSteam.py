import json
import requests

class scrapeSteam:
    def __init__(self, gID):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
        self.url = "https://store.steampowered.com/api/appdetails?appids="+gID+"&cc=in"
        self.page = requests.get(self.url, headers=self.headers)
        self.data = self.page
        self.data = self.data.json()
        self.gameID = gID

    def getGameName(self):
        name = str(self.data[self.gameID]['data']['name'])
        
        #print(name)

        return name
    
    def getGamePrice(self):
        if(self.data[self.gameID]['data']['is_free'] == True):
            print("The game is Free/Free to Play!")

            return -1.0
        else:
            price = float(self.data[self.gameID]['data']['price_overview']['final'])
            price /= 100

            #print(price)

            return price

#-----object creation example
#---------scrape = scrapeSteam("271590")
#---------scrape.getGameName()
#---------scrape.getGamePrice()