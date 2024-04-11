------------------------
# NOS News Web Scraper #
------------------------

This repository contains a python web scraper that will scrape Dutch words from the latest news articles on https://nos.nl/nieuws/laatste.


TODO:
    - Article method: Extract title, date/time of article, article ID, and other possibly useful information from article
    - Check for previous pickle file of Articles, if no matching article ID
        - Article method: Convert article text into list of words (all UPPERed and numbers filtered)
    - Once cycles through all Articles, load pickled articles and combine to create single list.
    - Pickle article list
    - Combine all word lists together to perform analysis