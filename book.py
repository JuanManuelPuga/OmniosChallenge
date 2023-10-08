from coinConversor import CoinConversor
from textGetter import TextGetter
from textTranslator import TextTranslator

class Book:
    #Function that initializes all the book's information.
    def __init__(self, ID, title, rating, price, imageURL):
        self.id = ID
        self.title = title
        self.rating = rating
        self.priceGBP = price[1:]
        self.imageURL = imageURL
        conversor = CoinConversor("GBP", "EUR", self.priceGBP)
        self.priceEUR = round(float(conversor.changeCoin()[0:-3]), 2)
        textGetter = TextGetter(self.title)
        self.originalText = textGetter.getText()
        textTranslator = TextTranslator(self.originalText)
        self.textESP = textTranslator.translateText("en", "es")
        self.textFR = textTranslator.translateText("en", "fr")