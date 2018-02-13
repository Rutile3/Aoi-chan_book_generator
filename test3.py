import requests
from bs4 import BeautifulSoup

print("台本化するurlを入力してください。")
#target_url = input()
target_url = "http://ncode.syosetu.com/n2634dg/1/"#デバッグ用

html = requests.get(target_url)#HTMLの取得
soup = BeautifulSoup(html.text, 'lxml') #要素を抽出

article_part = soup.find_all("div", {"id": "novel_honbun"})
soup.prettify()
