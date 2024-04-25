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
    for link in link_list:
        article_list.append(Article.fromScrape(link))
        delay = np.random.normal(mu, sigma)
        if delay<1: delay=1
        elif delay>6: delay=6
        time.sleep(delay)
    
    article_dict_list = [{"ID":article.ID, "url":article.url, "title":article.title, "date_time":article.date_time, "text":article.text} for article in article_list]
    json_string = json.dumps(article_dict_list)
    with open('articles_scrapped.json','w') as outfile:
        outfile.write(json_string)

def updateMasterList():
    master_article_list = []
    try:
        with open('master_article_list.json') as json_file:
            master_article_data = json.load(json_file)
            for article in master_article_data:
                master_article_list.append(Article(article['ID'], article['url'], article['title'], article['date_time'], article['text']))
    except:
        print("There is no existing Master Article list")
    
    # Retrieve list of scrapped articles and convert into Article objects
    scrapped_article_list = []
    try:
        with open('articles_scrapped.json') as json_file:
            scrapped_article_data = json.load(json_file)
            for article in scrapped_article_data:
                scrapped_article_list.append(Article(article['ID'], article['url'], article['title'], article['date_time'], article['text']))
    except:
        print("There is no existing Scrapped Article list")
    
    # See if newly scrapped articles exist already in master article list, if not then add them
    match_found=0
    for scrapped_article in scrapped_article_list:
        for master_article in master_article_list:
            if scrapped_article.ID == master_article.ID:
                match_found=1
                break
        if match_found == 0:
            master_article_list.append(scrapped_article)
        elif match_found == 1:
            match_found = 0
    article_dict_list = [{"ID":article.ID, "url":article.url, "title":article.title, "date_time":article.date_time, "text":article.text} for article in master_article_list]
    json_string = json.dumps(article_dict_list)
    with open('master_article_list.json','w') as outfile:
        outfile.write(json_string)