'''Seed the Mongo 'products' collection with products scraped from REI.com'''

from lib.mongo_conn import client as mongo_client
from data.scrape_products import all_products

# Connect to the 'products' collection
db = mongo_client['gearview-db']
products = db['products']

# Delete the existing products in the collection
products.delete_many({})

try:
    results = products.insert_many(all_products, ordered=True)
    
    print(f"Inserted {len(results.inserted_ids)} products.")
except Exception as e:
    print(e)