from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

import os
connectionString = os.environ.get("MONGO_URI")

client = MongoClient(connectionString)
