import FScrape
import json

class Article():
    
    def __init__(self,url):
        self.__url = url
        self.__soup, self.__html = FScrape.soupTextFromURL(self.__url)
        self.__title = self.__soup.title.text
        for script in self.__soup.find_all('script'):
            try:
                json_data = json.loads(script.text)
                self.__text = json_data['articleBody']
                self.__ID = json_data["identifier"]
                self.__date_time = json_data["datePublished"]
            except:
                pass
    
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