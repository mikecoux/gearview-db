# REI.com scraper

### To install the project dependencies...
*from the root directory*  

    pipenv install && pipenv shell
&nbsp;

## Instructions:

1. Delete Cloudinary images folder ("rei_images")
2. Push images to Cloudinary - this will run the product scraper, encode the images, and push new images to Cloudinary
3. Seed products - this will run the product scraper , fetch Cloudinary image links, and create new products in the Mongo "products" collection that contain corresponding Cloudinary image urls
4. Seed reviews - this will create 200 new reviews in the Mongo "reviews" collection with associated product Ids
5. Clear the Algolia index ("gearview-products")
6. Push new products to Algolia