from logging import exception
from bs4 import BeautifulSoup as bs
import requests
import csv
from time import sleep
import helper
import time

file = open('Guardian Medication Prices.csv', 'w')
writer = csv.writer(file)
writer.writerow(["Medications"])
writer.writerow(["Name", "Price"])

links = ["https://www.guardian.com.sg/health/vitamins-and-supplements/c/vitamins-supplements?page={}", 
"https://www.guardian.com.sg/health/cough-cold-and-allergy/c/cough-cold-and-allergy?page={}", 
"https://www.guardian.com.sg/health/beauty-enhancer-and-slimming/c/beauty-enhancer-and-slimming?page={}",
"https://www.guardian.com.sg/health/diabetic-and-nutrition/c/diabetic-and-nutrition?page={}",
"https://www.guardian.com.sg/health/health-aids-and-equipment/c/health-aids-and-equipments?page={}",
"https://www.guardian.com.sg/health/pain-and-fever/c/pain-and-fever?page={}"]

print("Medication \n")
dict = {}

for link in links:
    i = 0
    while(True):
        try:
            url = link.format(i)
            r = requests.get(url)
            soup = bs(r.content, 'html.parser')

            #if 0 items found, then end program
            try:
                test = soup.find('div', {'class': 'totalResults'}).text
                break
            except:
                pass


            # page number
            print("\n-----------" , (i+1) , "-----------\n")

            #get products from page
            for product in soup.find_all('div', {'class': 'product_content'}):
                product_name = product.find('h2', {'class': 'prod_description'}).text.strip()
                try:
                    product_price = product.find('p', {'class': 'price'}).text.strip()
                    dict[product_name] = float(product_price.replace("$", ""))
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