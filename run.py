from sklearn.feature_extraction.text import TfidfVectorizer
import requests, json
from classes import Provider


cnn = Provider("cnn", "top")
cnn.getarticles()
cnn.printarticles()


"""
#Returns json containing status/source/sort/articles
def getjson():
    #CNN
    cnn_url = "https://newsapi.org/v1/articles?source=cnn&sortBy=top&apiKey="
    cnn = requests.get(cnn_url + news_key)
    cnn_data = cnn.json()

    #wsj
    wsj_url = "https://newsapi.org/v1/articles?source=the-wall-street-journal&sortBy=top&apiKey="
    wsj = requests.get(wsj_url + news_key)
    wsj_data = wsj.json()

    #AP
    ap_url = "https://newsapi.org/v1/articles?source=associated-press&sortBy=top&apiKey="
    ap = requests.get(ap_url + news_key)
    ap_data = ap.json()

    return [cnn_data, wsj_data, ap_data]

def gettext():
    news_response = getjson()
    cnn_article_text = []
    ap_article_text = []
    wsj_article_text = []

    for jsonbody in news_response:
        for article_details in jsonbody["articles"]:
            print (article_details["description"] + '\n')



gettext()
"""
