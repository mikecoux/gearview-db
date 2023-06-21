'''Pull records from MongoDB, structure the data, and then send to Algolia'''

from lib.mongo_conn import client as mongo_client
from lib.algolia_conn import client as algolia_client

# Connect to Mongo 'products' collection
db = mongo_client['gearview-db']
products = db['products']

# Connect to Algolia 'products' index
index = algolia_client.init_index("gearview_products")

# Pull all products and push to Algolia
try:
    for product in products.find():
        record = {
            "objectID": product['_id'],
            "brand": product['brand'],
            "title": product['title'],
            "gender": product['gender'],
            "price": product['price'],
            "avg_rating": product['rei_avg_rating']
        }
        index.save_object(record).wait()
        
except Exception as e:
    print(e)
