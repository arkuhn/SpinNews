from sklearn.feature_extraction.text import TfidfVectorizer
import requests, json
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


"""
for provider in providers:
    print(provider.source)
    provider.getarticles()
    if (provider.articles):
        for article in provider.articles:
            print(article.description)
            print('\n')
        print("#########################")
"""

times_string = article_index["time"][1].description
wsj_string = article_index["the-wall-street-journal"][3].description
nyt_string = article_index["the-new-york-times"][1].description

vect = TfidfVectorizer(min_df=1)
tfidf = vect.fit_transform([times_string,
                             wsj_string,
                             nyt_string])
print((tfidf * tfidf.T).A)
