: : Run Jupyter notebook
cd
call C:\Users\mikey\AppData\Local\Continuum\anaconda3\Scripts\activate.bat environment_name
: : TODO NEED TO FIND LOCATION OF CONDA ENV

cd C:\Users\mikey\OneDrive\OLD\Documents\Coding projects\Foreign_Vocab_Web_Scraper

git add .

git commit -m "daily run: %date:~-4%%date:~3,2%%date:~0,2%.%time:~0,2%%time:~3,2%%time:~6,2%"

git push origin "main"