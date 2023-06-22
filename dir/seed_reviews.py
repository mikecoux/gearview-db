'''Assign products ids and push reviews to Mongo'''

from lib.mongo_conn import client as mongo_client
from data.fake_reviews import fake_reviews
from random import choice as rc

# Connect to the 'products' collection
db = mongo_client['gearview-db']
products = db['products']

# Get all product IDs and append them to a new list
ids = []
for id in products.find({},{"_id":1}):
    ids.append(str(id['_id']))
    
# Assign each review a random product id
for review in fake_reviews:
    review['product_id'] = rc(ids)

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