from algoliasearch.search_client import SearchClient

client = SearchClient.create("5D3D94T0SR", "135ada3f74a82b75019527647592b77c")

try:
    index = client.init_index('test_index')
    print("Algolia client connected.")
except Exception as e:
    print(e)