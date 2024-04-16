------------------------
# NOS News Web Scraper #
------------------------

This repository contains a python web scraper that will scrape Dutch words from the latest news articles on https://nos.nl/nieuws/laatste.


TODO:
    - Use new cleaned article __init__ function to load in articles from master_article_list.json
    - Article method: Convert article text into list of words (all UPPERed and numbers filtered)
    - Once cycles through all Articles, load jsoned articles and combine to create single list.
    - Combine all word lists together to perform analysis

BUGS TO FIX:
    - webScraper script is ignoring slicer which limits scrape to just 1 time