import requests
from bs4 import BeautifulSoup

target_url = "http://ncode.syosetu.com/n2634dg/1/"
html = requests.get(target_url)         #requestsを使って、webから取得

soup = BeautifulSoup(html.text,"lxml")

#article_part = soup.find_all("div", {"id": "novel_honbun"})
article_part = soup.find_all("div")
article = article_part[0].get_text()
print(article)