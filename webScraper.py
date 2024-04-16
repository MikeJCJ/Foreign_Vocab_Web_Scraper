import FScrape
from Article import Article
import numpy as np
import json
import time

# INPUTS
nos_latest_news_url = "https://nos.nl/nieuws/laatste"
mu, sigma = 3,2 # Scraper delay variables

def webDataScrape():
    # Get list of links from NOS latest news page
    nos_news_soup, nos_news_html = FScrape.soupTextFromURL(nos_latest_news_url)
    #writeStringToFile(nos_news_html, "output.txt")
    link_list = FScrape.getListArticleLinks(nos_news_soup)

    # Create Aricle objects
    article_list = []
    for link in link_list[0:2]:
        article_list.append(Article.fromScrape(link))
        delay = np.random.normal(mu, sigma)
        if delay<1: delay=1
        elif delay>6: delay=6
        time.sleep(delay)
    
    article_dict_list = [{"ID":article.ID, "url":article.url, "title":article.title, "date_time":article.date_time, "text":article.text} for article in article_list]
    json_string = json.dumps(article_dict_list)
    with open('articles_scrapped.json','w') as outfile:
        outfile.write(json_string)
    
    return article_dict_list