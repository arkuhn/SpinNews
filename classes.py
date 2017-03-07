from keys import NEWSAPI_KEY
import requests, json

class Article:
    author = None
    title = None
    description = ""
    url = None
    url_to_image = None
    published_at = None

    def __init__(self, author, description, title, url, url_to_image, published_at):
          self.author = author
          self.description = description
          self.title = title
          self.url = url
          self.url_to_image = url_to_image
          self.published_at = published_at

class Provider:
    status = None
    articles = None
    sort = None
    source = None

    def getarticles(self):
        self.articles = []

        provider_url = "https://newsapi.org/v1/articles?source=" + self.source + "&sortBy=" + self.sort + "&apiKey="
        provider = requests.get(provider_url + NEWSAPI_KEY)
        provider_data = provider.json()

        self.status = provider_data["status"]
        try:
            for article in provider_data["articles"]:
                description = article["description"]
                title = article["title"]
                published_at = article["publishedAt"]
                author = article["author"]
                url = article["url"]
                url_to_image = article["urlToImage"]

                new_article = Article(author, description, title, url, url_to_image, published_at)
                self.articles.append(new_article)
        except Exception:
            pass

            
    def printarticles(self):
        for article in self.articles:
            print (article.description )

    def __init__(self, source, sort):
          self.source = source
          self.sort = sort
