import FScrape
from Article import Article

# INPUTS
nos_latest_news_url = "https://nos.nl/nieuws/laatste"

if __name__=="__main__":
    # Get list of links from NOS latest news page
    nos_news_soup, nos_news_html = FScrape.soupTextFromURL(nos_latest_news_url)
    #writeStringToFile(nos_news_html, "output.txt")
    link_list = FScrape.getListArticleLinks(nos_news_soup)

    # Create Aricle objects
    article_list = []
    for link in link_list:
        article_list.append(Article(link))
    