from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
import random as rd

URL = "https://www.drinktrade.com/coffee/all-coffee"
baseUrl = "https://www.drinktrade.com"

driver = webdriver.Chrome("/Users/laurajurgensmeier/Desktop/extreme-coffee-experience/products/src/main/scraper/chromedriver")
driver.get(URL)

soup = BeautifulSoup(driver.page_source, "html.parser")

allLinks = soup.findAll('a', class_="product-link")
for link in allLinks:
    print(link.get("href"))

driver.quit()

def getProductInformation(pUrl):
    URL = "https://www.drinktrade.com/coffee/all-coffee"
    driver = webdriver.Chrome("/Users/laurajurgensmeier/Desktop/extreme-coffee-experience/products/src/main/scraper/chromedriver")
    driver.get(baseUrl + pUrl)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    name = soup.find("h1", class_="product-nameV2 text-display-2-mobile text-display-2-desktop").text
    flavor = soup.find("h3", class_="product__taste-group").text
    flavorNotes = soup.find("div", class_="product-card__flavorNotes").text
    description = soup.find("div", class_="description-container text-body-2-mobile text-body-2-desktop").text
    location = soup.find("h3", class_="roaster-location").text
    roaster = soup.find("h2", class_="roaster-nameV2").text
    imgURL = soup.find("img", class_="roaster-product-image").get("src")
    roastLevel = soup.findAll("div", class_="detail-icon")[1].find("img").get("src")
    roastLevel = int(roastLevel.replace(".svg", "").split("_")[-1])
    roasterNotes = soup.find("div", class_="roaster-notes-body").text
    price = float(f"{rd.randrange(16, 28)}.{rd.randrange(0, 95, 5)}")

    productData = [name, flavor, flavorNotes, description, location, roaster, imgURL, roastLevel, roasterNotes, price]

    driver.quit()

    return productData

header = ['name', 'flavor', 'flavorNotes', 'description', 'location', 'roaster', 'imageURL', 'roastLevel', 'roasterNotes', 'price']


with open('products.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    writer.writerow(header)

    for link in allLinks:
        writer.writerow(getProductInformation(link.get("href")))

    writer.writerow(getProductInformation("/enchanted/p/3105"))
    writer.writerow(getProductInformation("/compass/p/3432"))
    writer.writerow(getProductInformation("/black-bear-blend/p/373"))
    writer.writerow(getProductInformation("/washington-blend/p/4103"))
    writer.writerow(getProductInformation("/big-city/p/3001"))
    writer.writerow(getProductInformation("/71-irving-house-blend/p/100"))
    writer.writerow(getProductInformation("/los-altos-mcpbbzzt/p/4067"))
    writer.writerow(getProductInformation("/vista-hermosa/p/4260"))
    writer.writerow(getProductInformation("/guatemala-los-santos-zqyieicz/p/4234"))
    writer.writerow(getProductInformation("/cold-brew-lnaxdsex/p/925"))
    writer.writerow(getProductInformation("/toketee/p/476"))
    writer.writerow(getProductInformation("/toni/p/3203"))
    writer.writerow(getProductInformation("/power-glory-blend/p/3366"))
    writer.writerow(getProductInformation("/h-o-m-e-s-blend/p/2160"))
    writer.writerow(getProductInformation("/blush-berry/p/4294"))
