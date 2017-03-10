import requests
from classes import Provider, Article

article_index = {}

def getproviders():
    sources_url = "https://newsapi.org/v1/sources?language=en&country=us"
    source = requests.get(sources_url)
    source_data = source.json()
    for source in source_data["sources"]:
        provider_id = source["id"]
        new_provider = Provider(provider_id, "top")
        new_provider.getarticles()
        article_index[new_provider.source] = new_provider.articles

getproviders()


for provider in article_index:
    print("Provider: " + provider + '\n')
    for article in article_index[provider]:
        print("Article: " + article.description + '\n')
    print("#########################\n")
