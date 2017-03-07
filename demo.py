from sklearn.feature_extraction.text import TfidfVectorizer
from keys import NEWSAPI_KEY
import requests
import json


news_key = NEWSAPI_KEY
url = "https://newsapi.org/v1/articles?source=the-next-web&sortBy=latest&apiKey="
r = requests.get(url + news_key)
json_response = r.json()
print(json.dumps(json_response, indent=4))


print("hello world")
