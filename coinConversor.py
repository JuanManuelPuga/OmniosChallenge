import requests
from bs4 import BeautifulSoup

class CoinConversor:
    def __init__(self, srcCoin, trgCoin, amount):
        self.srcCoin = srcCoin
        self.trgCoin = trgCoin
        self.amount = float(amount)

    def changeCoin(self):
        URL = "https://www.x-rates.com/calculator/"
        #Creating a payload to post information in the URL.
        payload = {'amount': self.amount, 'from': self.srcCoin, 'to': self.trgCoin}
        response = requests.post(URL, data=payload)
        soup = BeautifulSoup(response.content, 'html.parser')
        result = soup.find("span", class_= "ccOutputRslt").get_text(strip=True)
        return result