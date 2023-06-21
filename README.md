# REI.com scraper

### To install the project dependencies...
*from the root directory*  

    pipenv install && pipenv shell
&nbsp;

## Scripts

### Scrape data from REI.com and upload to a MongoDB collection
*from the dir directory*

    python push_mongo.py
### Pull documents from the 'products' collection and create records in Algolia
*from the dir directory*

    python push_algolia.py

### Download images from REI and save them locally

### Upload images from local storage to Cloudinary
