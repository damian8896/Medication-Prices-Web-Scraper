from bs4 import BeautifulSoup as bs
import requests
import csv
import helper
from time import sleep

file = open('Raffles Medication and Services Prices.csv', 'w')
writer = csv.writer(file)
writer.writerow(["Medications"])
writer.writerow(["Name", "Price"])

i = 1

dict = {}

print("Medication \n")
while(True):
    try:
        url = "https://www.raffleshealth.com/all-products.html?p={}".format(i)
        r = requests.get(url)
        soup = bs(r.content, 'html.parser')
        page_number = soup.find('li', {'class': 'item current'}).find_all('span')[1].text

        #if page number doesn't match query parameter, limit has been reached
        if(int(page_number) != i):
            break

        #page number
        print("\n-----------" + page_number + "-----------\n")

        #get products from page
        for product in soup.find_all('div', {'class': 'product details product-item-details'}):
            product_name = product.find('a').text.strip()
            try:
                product_price = product.find('span', {'class': 'price'}).text.strip()
                dict[product_name] = float(product_price.replace("$", ""))
                writer.writerow([product_name, product_price])
                print(product_name + " : " + product_price)
            except:
                continue
        
        sleep(2)
        i += 1
    except:
        break

writer.writerow([])
writer.writerow(["Services"])
writer.writerow(["Name", "Price"])

helper.find_stats(dict)

i = 1

print("\nServices \n")
dict = {}

while(True):
    try:
        url = "https://www.raffleshealth.com/services.html?p={}".format(i)
        r = requests.get(url)
        soup = bs(r.content, 'html.parser')
        page_number = soup.find('li', {'class': 'item current'}).find_all('span')[1].text

        #if page number doesn't match query parameter, limit has been reached
        if(int(page_number) != i):
            break

        #page number
        print("\n-----------" + page_number + "-----------\n")

        #get services from page
        for service in soup.find_all('div', {'class': 'product details product-item-details'}):
            service_name = service.find('a').text.strip()
            try:
                service_price = service.find('span', {'class': 'price'}).text.strip()
                dict[service_name] = float(service_price.replace("$", ""))
                writer.writerow([service_name, service_price])
                print(service_name + " : " + service_price)
            except:
                continue
        
        sleep(2)
        i += 1
    except:
        break

helper.find_stats(dict)
file.close()