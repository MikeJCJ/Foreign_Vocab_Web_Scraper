class Article():
    
    def __init__(self,url):
        self.__url = url
        self.__article_title = None
        self.__article_ID = None
    
    @property
    def url(self):
        return self.__url