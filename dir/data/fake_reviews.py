'''Create fake reviews'''

from random import randint
from faker import Faker

fake = Faker()

def create_reviews():
    
    reviews = []
    usernames = []

    # Create 200 reviews
    for i in range(200):
        
        # create unique usernames 
        username = fake.first_name().lower()
        while username in usernames:
            username = fake.first_name().lower()
        usernames.append(username)
        
        # add a rating between 1 and 5
        rating = randint(1,5)
        
        # add between -10 and 10 votes
        num_votes = randint(-4, 10)
        
        # create a fake review description with 3 sentences
        description = fake.paragraph(nb_sentences=3)
        
        new_review = {
            "username": username,
            "rating": rating,
            "description": description,
            "num_votes": num_votes,
            "voting_users" : []
        }
        
        reviews.append(new_review)
    
    return reviews

fake_reviews = create_reviews()