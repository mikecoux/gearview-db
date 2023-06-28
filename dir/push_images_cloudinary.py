'''STEP ONE: Push images to cloudinary whose image id matches the REI src URL'''

import requests
import base64
import json
from data.scrape_products import all_products

from dotenv import load_dotenv
load_dotenv()

import cloudinary
from cloudinary import uploader

# get reference to config instance
config = cloudinary.config(secure=True)

encoded_images = []

# required in the get request
headers = {'user-agent': 'my-app/0.0.1'}

for product in all_products:
    
    # iterate over each image url pulled from REI.com and encode it
    for image in product['rei_images']:
        
        # grab the filename to use as the id in cloudinary
        name = image.split('/')[-1].split('.')[0]
        
        # binary encode the image
        uri = base64.b64encode(requests.get(image, headers=headers).content).decode('utf-8')
        
        # grab the extention for use in the data uri
        ext = image.split('/')[-1].split('.')[-1]
        
        new_image = {
            "name": name,
            "uri": uri,
            "ext": ext
        }
        
        encoded_images.append(new_image)
            
for image in encoded_images:
    # construct the data uri
    data_uri = f"data:image/{image['ext']};base64," + image['uri']
    
    # keep the original filename when uploading to cloudinary
    # add images to a specific folder in cloudinary
    upload = uploader.upload(data_uri, 
        public_id = image['name'],
        unique_filename = False,
        folder = "rei_images")
    
    print("**** Base 64 Data URI ****\nDelivery URL: ", json.dumps(upload,indent=2), "\n")