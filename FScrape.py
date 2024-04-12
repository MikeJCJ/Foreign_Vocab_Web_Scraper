from bs4 import BeautifulSoup
import requests
import re

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
        if re.match(r"/artikel/", link_url):
            link_list.append("https://nos.nl"+link_url)
    return link_list