'''STEP 3: Assign products ids and push reviews to Mongo'''

from lib.mongo_conn import client as mongo_client
from data.fake_reviews import fake_reviews
from random import choice as rc

# Connect to the 'products' collection
db = mongo_client['gearview-db']
products = db['products']
all_products = products.find()

# Get all product IDs and append them to a new list
ids = []
products_list = []
for product in all_products:
    ids.append(str(product['_id']))
    products_list.append(product)
        
# Assign each review a random product id
for review in fake_reviews:
    review['product_id'] = rc(ids)
    
# Create a dictionary for quick lookup
products_dict = { str(product['_id']): product for product in products_list }


# for key in products_dict.keys():
#     print(key)

# print(products_dict.get('649c764c790d643fa03e186b'))
    
# Find matching products
for review in fake_reviews:
    if review['product_id'] in products_dict:
        review['product_brand'] = products_dict[review['product_id']]['brand']
        review['product_title'] = products_dict[review['product_id']]['title']    

# Connect to the 'reviews' collection
reviews = db['reviews']

# Delete all existing reviews in the collection
reviews.delete_many({})
    
try:
    # this option prevents additional documents from being inserted if one fails
    results = reviews.insert_many(fake_reviews, ordered=True)
    
    print(f"Inserted {len(results.inserted_ids)} reviews.")
except Exception as e:
    print(e)