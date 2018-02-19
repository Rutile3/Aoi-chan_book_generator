import requests
from bs4 import BeautifulSoup

target_url = "http://ncode.syosetu.com/n2634dg/1/"
r = requests.get(target_url)         #requestsを使って、webから取得
soup = BeautifulSoup(r.text, 'lxml') #要素を抽出

for i in soup.find_all('div'):
    if(i.get("id") == "novel_honbun"):
        print(i.string)
        break

input()