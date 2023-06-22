#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import json

headers = {'user-agent': 'my-app/0.0.1'}

def scrape_products():
    doc = BeautifulSoup(requests.get(
        "https://www.rei.com/c/mens-running-shoes?ir=category%3Amens-running-shoes&pagesize=90", headers=headers).text, 'html.parser')

    data = doc.select('.pPe0GNuagvmEFURs1Q_vm')
    
    # This doesn't work for some reason??
    # test = re.findall(r'[\d]+[.,\d]+|[\d]*[.][\d]+|[\d]+', data[0].select('.cdr-rating__caption-sr_12-1-0')[0].text)[1]
    
    products = []
    
    for product in data:
        new_product = {}
        
        new_product["brand"] = product.select('._1fwp3k8dh1lbhAAenp87CH')[0].text
        new_product["title"] = product.select('.r9nAQ5Ik_3veCKyyZkP0b')[0].text.split(' - ')[0]
        new_product["gender"] = product.select('.r9nAQ5Ik_3veCKyyZkP0b')[0].text.split(' - ')[-1]
        new_product["price"] = product.select('._1q8gG3vYPuFFDKIFSW2pT span')[0].text
        new_product["rei_avg_rating"] = ''.join([str for str in product.select('.cdr-rating__caption-sr_12-1-0')[0].text.split() if "." in str])
        new_product["rei_images"] = ["https://www.rei.com" + i.select('div img')[0]['src'] for i in product.select('._1WNEGe6yirBYtWb8nB4oeZ')[0]]
        new_product["rei_href"] = "https://www.rei.com" + product.select('a')[0]['href']

        products.append(new_product)
        
    return products

all_products = scrape_products()