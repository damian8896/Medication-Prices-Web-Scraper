from logging import exception
from bs4 import BeautifulSoup as bs
import requests
import csv
from time import sleep
import time
import helper

file = open('Pupsik Medication Prices.csv', 'w')
writer = csv.writer(file)
writer.writerow(["Medications"])
writer.writerow(["Name", "Price"])

i = 1
dict = {}

print("Medication \n")
while(True):
    try:
        url = "https://www.pupsikstudio.com/beauty-health?p={}".format(i)

        r = requests.get(url)
        soup = bs(r.content, 'html.parser')
        end = False
        try:
            #if 0 items found
            test = soup.find('div', {'class': 'message info empty'}).text
            break
        except:
            pass

        # page number
        print("\n-----------" , i , "-----------\n")

        #get products from page
        for product in soup.find_all('div', {'class': 'product details product-item-details'}):
            product_name = product.find('a', {'class': 'product-item-link'}).text.strip()
            try:
                product_price = product.find('span', {'class': 'price'}).text.strip()
                dict[product_name] = float(product_price.replace("S$", ""))
                writer.writerow([product_name, product_price])
                print(product_name + " : " + product_price)
            except:
                continue
        
        sleep(2)
        i += 1
    except exception:
        print(exception)
        break

helper.find_stats(dict)
file.close()