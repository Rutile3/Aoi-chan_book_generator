import requests
from bs4 import BeautifulSoup

target_url = "http://ncode.syosetu.com/n2634dg/1/"
html = requests.get(target_url)         #requestsを使って、webから取得

soup = BeautifulSoup(html.text,"lxml")

article_part = soup.find_all("div", {"id": "novel_honbun"})
article = soup.article_part.string
print(article)