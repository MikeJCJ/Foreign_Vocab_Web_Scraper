from bs4 import BeautifulSoup
import requests
import re

# INPUTS
nos_latest_news_url = "https://nos.nl/nieuws/laatste"


def soupTextFromURL (url:str) -> BeautifulSoup:
    '''Take news url and turn into html soup'''
    url_response = requests.get(url)
    output_soup = BeautifulSoup(url_response.text, 'html.parser')
    return output_soup, url_response.text

def writeStringToFile(input_string:str, file_out:str):
    '''Write html to text document'''
    with open(file_out, "a") as f:
        f.write(input_string)

def getListArticleLinks(soup:BeautifulSoup) -> list:
    link_list = []
    for link in soup.find_all('a'):
        link_url = link.get('href')
        print(f"link: {link_url}")
        if re.match(r"/artikel/", link_url):
            link_list.append("https://nos.nl"+link_url)
    return link_list



if __name__=="__main__":
    nos_news_soup, nos_news_html = soupTextFromURL(nos_latest_news_url)
    #writeStringToFile(nos_news_html, "output.txt")
    link_list = getListArticleLinks(nos_news_soup)
    print(link_list)