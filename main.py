import FScrape
from Article import Article
import json

# INPUTS
nos_latest_news_url = "https://nos.nl/nieuws/laatste"

if __name__=="__main__":
    # Get list of links from NOS latest news page
    nos_news_soup, nos_news_html = FScrape.soupTextFromURL(nos_latest_news_url)
    #writeStringToFile(nos_news_html, "output.txt")
    link_list = FScrape.getListArticleLinks(nos_news_soup)

    # Create Aricle objects
    article_list = []
    for link in link_list[0:1]: # TODO REMOVE SLICER
        article_list.append(Article(link))
        print(f"link: {link}")
    
    for article in article_list:
        article_soup, article_html = FScrape.soupTextFromURL(article.url)
        print(f"title: {article_soup.title.text}")
        script_elements = article_soup.find_all('script')
        for script in script_elements:
            try:
                json_data = json.loads(script.text)
                article_body = json_data['articleBody']
                print(F"article_text: {article_body}")
            except:
                pass