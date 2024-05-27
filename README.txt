------------------------
# NOS News Web Scraper #
------------------------

Key Skills: Python Webscraping | Language Data Processing

This repository contains a python web scraper that will scrape Dutch words from the latest news articles on https://nos.nl/nieuws/laatste.

- Process -
1 - Run scraper_controller.ipynb to scrape all latest articles from the nos.nl website.
2 - Check word_list_filtered.csv for any invalid words (names, companies etc) or words which the user has already learned.
    - Add these words to invalid_words.csv and learned_words.csv.
3 - Re-run every couple days to get more accurate top 1000 words or to refresh word list due to filters.


- To do -
    - Create python script with all code from notebook
    - Script will also have a 'last datetime run' var
    - bat will launch when pc is turned on.
    - If last datetime is more than 1 day ago, python script will run