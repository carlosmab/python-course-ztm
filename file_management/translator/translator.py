from translate import Translator

translator = Translator(to_lang="es")

with open("text_to_translate.txt", mode="r") as f:
    text = f.read()
    
translated_text = translator.translate(text)    

with open("translation.txt", mode="w") as f:
    f.write(translated_text)
    
print(translated_text)

import requests
from bs4 import BeautifulSoup


res = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.body)