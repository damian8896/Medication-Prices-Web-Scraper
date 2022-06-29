from logging import exception
import unicodedata
from bs4 import BeautifulSoup as bs
import requests
import csv
import helper
from time import sleep
import time

file = open('Watsons Medication Prices.csv', 'w')
writer = csv.writer(file)
writer.writerow(["Medications"])
writer.writerow(["Name", "Price"])

i = 0
dict = {}

print("Medication \n")
while(True):
    try:
        url = "https://www.watsons.com.sg/health/c/2100000?page={}".format(i)

        r = requests.get(url, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"})
        soup = bs(r.content, 'html.parser')
        end = soup.find('div', {'class': 'page hidden-xs hidden-sm'}).find('span', {'class': 's2'}).text

        #if 0 items found, then end program
        if(int(end) == 0):
            break

        # page number
        print("\n-----------" , (i+1) , "-----------\n")

        #get products from page
        for product in soup.find_all('div', {'class': 'productNameInfo'}):
            product_name = unicodedata.normalize("NFKD",product.find('h3').text.strip())
            try:
                product_price = product.find('div', {'class': 'h2'}).text.strip()
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