'''STEP 2: Seed the Mongo 'products' collection with products scraped from REI.com'''
from dotenv import load_dotenv
load_dotenv()
import os

from lib.mongo_conn import client as mongo_client
from data.scrape_products import all_products
import re

# Connect to the 'products' collection
db = mongo_client['gearview-db']
products = db['products']

# Delete the existing products in the collection
products.delete_many({})

# Pull in the cloudinary base url
cloud_base_url = os.environ.get("CLOUDINARY_BASE")

# Iterate through each product and change the url prefix to
# the cloudinary base while keeping the id
try:
    for product in all_products:
        images = product['rei_images']
        
        for i in range(len(product['rei_images'])):
            id = re.search("(?<=media\/)(.*)(?=\.jpg)", images[i])[0]
            newUrl = cloud_base_url + id + '.jpg'
            images[i] = newUrl
                
    results = products.insert_many(all_products, ordered=True)
    
    print(f"Inserted {len(results.inserted_ids)} products.")
    
except Exception as e:
    print(e)