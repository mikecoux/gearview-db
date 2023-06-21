from algoliasearch.search_client import SearchClient
from dotenv import load_dotenv
load_dotenv()

import os
app_id = os.environ.get("ALGOLIA_APP_ID")
write_key = os.environ.get("ALGOLIA_WRITE_KEY")


client = SearchClient.create(app_id, write_key)

try:
    index = client.init_index('test_index')
    print(f"Algolia App #{index.app_id} connected.")
except Exception as e:
    print(e)