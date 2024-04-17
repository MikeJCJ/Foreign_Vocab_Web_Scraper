import FScrape
import json

class Article():
    
    def __init__(self, ID, url, title, date_time, text):
        self.__ID = ID
        self.__url = url
        self.__title = title
        self.__date_time = date_time
        self.__text = text

    @property
    def url(self):
        return self.__url
    
    @property
    def soup(self):
        return self.__soup
    
    @property
    def html(self):
        return self.__html
    
    @property
    def title(self):
        return self.__title
    
    @property
    def text(self):
        return self.__text
    
    @property
    def ID(self):
        return self.__ID
    
    @property
    def date_time(self):
        return self.__date_time
    
    @classmethod
    def fromScrape(cls, url):
        soup, html = FScrape.soupTextFromURL(url)
        title = soup.title.text
        for script in soup.find_all('script'):
            try:
                json_data = json.loads(script.text)
                text = json_data['articleBody']
                ID = json_data["identifier"]
                date_time = json_data["datePublished"]
            except:
                pass
        return cls(ID, url, title, date_time, text)
    
    def retrieveWordList():
        pass