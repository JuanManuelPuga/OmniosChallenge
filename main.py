import requests
from bs4 import BeautifulSoup
from book import Book
import json

#Acces to retrieve the number of pages from the website.
URL = "http://books.toscrape.com"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
nPages = int(soup.find("li", class_="current").text.split()[-1])

#Initializing variables.
URL = "http://books.toscrape.com/catalogue/page-"
bookList = []
counter = 0

for page in range(1, (nPages + 1)):

    act_page = requests.get(URL + str(page) + ".html")
    act_soup = BeautifulSoup(act_page.content, "html.parser")
    #Fetch the element that contains the books information from the current page.
    results = act_soup.find("ol", class_="row")
    books = results.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
    #Loop to create a Book object for every book that contains all the book information.
    for book in books:
        image_url = book.find("div", class_="image_container").find("a")["href"]
        rating = book.find("p")["class"][1]
        title = book.find("h3").find("a")["title"]
        price = book.find("div", class_="product_price").find("p", class_="price_color").text.strip()
        bookList.append(Book(counter, title, rating, price, image_url))
        counter = counter + 1

#Exportation in JSON format of all the data to a .txt file.
with open('output.txt', 'w', encoding="utf-8") as f:
    for book in bookList:
        json_string = json.dumps(book.__dict__, ensure_ascii=False)
        f.write(json_string)
        f.write('\n')